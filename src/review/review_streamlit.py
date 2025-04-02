import streamlit as st
import json
import hashlib
from pathlib import Path
from PIL import Image, UnidentifiedImageError

from review_logic import (
    load_clusters,
    save_review_state,
    add_decision_to_cluster,
    filter_clusters_for_review,
    normalize_cluster_paths,
    merge_review_data,
)


def configure_page():
    st.set_page_config(page_title="SmartMedia Review UI", layout="wide")
    st.title("📷 SmartMedia Deduplication Review")
    st.markdown("Use the interface below to review and tag similar image clusters.")


def get_image_key(img_path: str) -> str:
    return hashlib.md5(img_path.encode()).hexdigest()


def load_and_merge_clusters(match_file, base_path_input, review_file_path):
    base_path = Path(base_path_input).expanduser().resolve()
    match_data = json.load(match_file)
    match_data = normalize_cluster_paths(match_data, base_path)

    if review_file_path.exists():
        reviewed_data = load_clusters(review_file_path)
        match_data = merge_review_data(match_data, reviewed_data)

    return match_data


def get_clusters_to_review(match_data):
    def is_reviewed(c):
        review = c.get("review", {})
        return review.get("summary") not in (None, "uncertain")

    return [c for c in match_data if not is_reviewed(c)]


def render_cluster_selector(total_clusters):
    if "last_cluster_idx" not in st.session_state:
        st.session_state.last_cluster_idx = 0
    else:
        st.session_state.last_cluster_idx = min(st.session_state.last_cluster_idx, total_clusters - 1)

    cluster_idx = st.number_input(
        "Select Cluster to Review",
        min_value=1,
        max_value=total_clusters,
        step=1,
        value=st.session_state.last_cluster_idx + 1,
        format="%d",
        key="cluster_index_selector"
    ) - 1

    st.session_state.last_cluster_idx = cluster_idx
    return cluster_idx


def apply_pending_rotations(files):
    for f in files:
        img_id = get_image_key(f["path"])
        rotate_key = f"rotate_{img_id}"
        pending_key = f"pending_rotation_{img_id}"

        if rotate_key not in st.session_state:
            st.session_state[rotate_key] = 0

        if pending_key in st.session_state:
            st.session_state[rotate_key] = (st.session_state[rotate_key] + st.session_state[pending_key]) % 360
            del st.session_state[pending_key]


def render_image_controls(col, f):
    img_path = f.get("path", "")
    img_name = f.get("name", "")
    img_id = get_image_key(img_path)

    rotate_key = f"rotate_{img_id}"
    decision_key = f"decision_{img_id}"
    button_left_key = f"btn_left_{img_id}"
    button_right_key = f"btn_right_{img_id}"

    try:
        img = Image.open(img_path)
        rotated_img = img.rotate(st.session_state[rotate_key], expand=True)
        col.image(rotated_img, use_container_width=True, caption=img_name)

        # Rotation buttons
        left_col, right_col = col.columns([1, 1])
        with left_col:
            if st.button("↺ Rotate Left", key=button_left_key):
                st.session_state[f"pending_rotation_{img_id}"] = 90
                st.rerun()  # 👈 immediate application
        with right_col:
            if st.button("↻ Rotate Right", key=button_right_key):
                st.session_state[f"pending_rotation_{img_id}"] = -90
                st.rerun()

        col.radio(
            "Decision",
            ["uncertain", "keep", "delete", "merge"],
            key=decision_key,
            horizontal=True
        )

    except UnidentifiedImageError:
        col.warning(f"⚠️ Invalid image: {img_path}")
    except Exception as e:
        col.error(f"Error loading image: {img_path}\n\n{e}")


def render_review_form(cluster, files, match_data, review_file_path):
    rotation_map = {
        f.get("path"): st.session_state.get(f"rotate_" + get_image_key(f.get("path")), 0)
        for f in files
    }

    with st.form(key="review_form"):
        reviewer = st.text_input("Reviewer name (optional):")
        notes = st.text_area("Notes (optional):", key="review_notes")
        submitted = st.form_submit_button("Submit Review")

        if submitted:
            for f in files:
                img_id = get_image_key(f["path"])
                f["decision"] = st.session_state.get(f"decision_" + img_id, "uncertain")
                f["rotation"] = st.session_state.get(f"rotate_" + img_id, 0)

            reviewed_cluster = add_decision_to_cluster(
                cluster,
                reviewer=reviewer or None,
                notes=notes or None,
                rotation_map=rotation_map
            )
            match_data[cluster["index"]] = reviewed_cluster
            save_review_state(match_data, review_file_path)
            st.success(f"Cluster #{cluster['index']} tagged and saved.")
            st.rerun()


# -------------------------
# Main App Entry Point
# -------------------------

configure_page()
match_file = st.file_uploader("Upload a *_match_sorted.json file", type="json")
base_path_input = st.text_input("Base directory for images", value="~/Desktop/TRAINING_1-pics/")
review_file_path = Path("review_output.json")

if match_file:
    match_data = load_and_merge_clusters(match_file, base_path_input, review_file_path)
    clusters_to_review = get_clusters_to_review(match_data)
    total_clusters = len(clusters_to_review)

    if total_clusters == 0:
        st.success("✅ All clusters have been reviewed!")
    else:
        cluster_idx = render_cluster_selector(total_clusters)
        cluster = clusters_to_review[cluster_idx]
        files = cluster.get("files", [])

        st.caption(f"Photo Clusters to Review: {total_clusters}  •  Current Cluster: {cluster_idx + 1}")

        if not files:
            st.subheader(f"Cluster #{cluster['index']} — ⚠️ No valid files (skipped)")
            st.warning("This cluster has no usable image files after filtering. Try another.")
            st.stop()

        if st.session_state.get("last_rendered_idx") != cluster["index"]:
            st.session_state["review_notes"] = ""
            st.session_state["last_rendered_idx"] = cluster["index"]

        apply_pending_rotations(files)

        cols = st.columns(len(files))
        for col, f in zip(cols, files):
            render_image_controls(col, f)

        render_review_form(cluster, files, match_data, review_file_path)
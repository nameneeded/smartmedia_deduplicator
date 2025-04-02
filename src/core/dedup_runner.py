import argparse
import json
from pathlib import Path
from PIL import Image


def apply_rotation(image_path: Path, degrees: int, dry_run: bool):
    if degrees == 0:
        return
    if dry_run:
        print(f"[dry-run] Would rotate: {image_path} by {degrees}°")
        return
    try:
        img = Image.open(image_path)
        rotated = img.rotate(-degrees, expand=True)
        rotated.save(image_path)
        print(f"✅ Rotated: {image_path} by {degrees}°")
    except Exception as e:
        print(f"❌ Failed to rotate {image_path}: {e}")


def handle_deletion(image_path: Path, dry_run: bool):
    if dry_run:
        print(f"[dry-run] Would delete: {image_path}")
    else:
        try:
            image_path.unlink()
            print(f"🗑️ Deleted: {image_path}")
        except Exception as e:
            print(f"❌ Failed to delete {image_path}: {e}")


def process_review_file(review_path: Path, dry_run: bool):
    with open(review_path, "r", encoding="utf-8") as f:
        clusters = json.load(f)

    print(f"📂 Loaded {len(clusters)} clusters from {review_path.name}\n")

    for cluster in clusters:
        files = cluster.get("files", [])
        review = cluster.get("review", {})
        summary = review.get("summary", "uncertain")
        print(f"🔍 Cluster {cluster.get('index', '?')} — {summary.upper()}")

        for file in files:
            path = Path(file["path"]).expanduser().resolve()
            rotation = file.get("rotation", 0)
            decision = file.get("decision", "uncertain")

            if decision == "keep":
                apply_rotation(path, rotation, dry_run)

            elif decision == "delete":
                handle_deletion(path, dry_run)

            elif decision == "merge":
                print(f"[merge] ⏳ Manual merge needed for: {path}")

            elif decision == "uncertain":
                print(f"[skip] ❓ Uncertain decision for: {path}")

        print("---")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run deduplication actions from review file")
    parser.add_argument("--review-file", type=Path, required=True, help="Path to reviewed JSON output")
    parser.add_argument("--apply", action="store_true", help="Apply changes instead of dry-run")
    args = parser.parse_args()

    process_review_file(args.review_file, dry_run=not args.apply)

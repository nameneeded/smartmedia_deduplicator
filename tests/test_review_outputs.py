import pytest
from src.review.review_logic import add_decision_to_cluster

BASE = "/Users/jseanw/Desktop/TRAINING_1-pics"


def build_cluster():
    return {
        "files": [
            {"path": f"{BASE}/me_and_the_sphinx.jpg", "name": "me_and_the_sphinx.jpg"},
            {"path": f"{BASE}/1000003779 copy.jpg", "name": "1000003779 copy.jpg"},
            {"path": f"{BASE}/1000003779.jpg", "name": "1000003779.jpg"}
        ],
        "weight": 8,
        "index": 1
    }


def test_review_logic_dedup_cluster():
    cluster = build_cluster()
    rotation_map = {f["path"]: 0 for f in cluster["files"]}

    cluster["files"][0]["decision"] = "keep"
    cluster["files"][1]["decision"] = "delete"
    cluster["files"][2]["decision"] = "keep"

    reviewed = add_decision_to_cluster(cluster, reviewer="reviewer_name", notes="1 line notes", rotation_map=rotation_map)

    assert reviewed["review"]["summary"] == "dedup"
    assert reviewed["review"]["reviewer"] == "reviewer_name"
    assert reviewed["review"]["notes"] == "1 line notes"

    expected = {
        "me_and_the_sphinx.jpg": "keep",
        "1000003779 copy.jpg": "delete",
        "1000003779.jpg": "keep"
    }
    for f in reviewed["files"]:
        assert f["decision"] == expected[f["name"]]
        assert f["rotation"] == 0


def test_review_all_uncertain():
    cluster = build_cluster()
    for f in cluster["files"]:
        f["decision"] = "uncertain"
    rotation_map = {f["path"]: 0 for f in cluster["files"]}

    reviewed = add_decision_to_cluster(cluster, reviewer="anon", notes="Need review", rotation_map=rotation_map)
    assert reviewed["review"]["summary"] == "uncertain"
    assert reviewed["review"]["reviewer"] == "anon"
    for f in reviewed["files"]:
        assert f["decision"] == "uncertain"
        assert f["rotation"] == 0


def test_review_all_keep():
    cluster = build_cluster()
    for f in cluster["files"]:
        f["decision"] = "keep"
    rotation_map = {f["path"]: 0 for f in cluster["files"]}

    reviewed = add_decision_to_cluster(cluster, reviewer="keepbot", notes="All clean", rotation_map=rotation_map)
    assert reviewed["review"]["summary"] == "keep"
    for f in reviewed["files"]:
        assert f["decision"] == "keep"


def test_review_all_delete():
    cluster = build_cluster()
    for f in cluster["files"]:
        f["decision"] = "delete"
    rotation_map = {f["path"]: 0 for f in cluster["files"]}

    reviewed = add_decision_to_cluster(cluster, reviewer="purger", notes="Remove all", rotation_map=rotation_map)
    assert reviewed["review"]["summary"] == "delete"
    for f in reviewed["files"]:
        assert f["decision"] == "delete"


def test_review_merge_cluster():
    cluster = build_cluster()
    for f in cluster["files"]:
        f["decision"] = "merge"
    rotation_map = {f["path"]: 0 for f in cluster["files"]}

    reviewed = add_decision_to_cluster(cluster, reviewer=None, notes="Ready to combine", rotation_map=rotation_map)
    assert reviewed["review"]["summary"] == "merge"
    assert reviewed["review"].get("reviewer") is None
    for f in reviewed["files"]:
        assert f["decision"] == "merge"


def test_review_mixed_cluster():
    cluster = build_cluster()
    cluster["files"][0]["decision"] = "keep"
    cluster["files"][1]["decision"] = "merge"
    cluster["files"][2]["decision"] = "delete"
    rotation_map = {f["path"]: 0 for f in cluster["files"]}

    reviewed = add_decision_to_cluster(cluster, reviewer="tester", notes="Mixed call", rotation_map=rotation_map)
    assert reviewed["review"]["summary"] == "mixed"
    for f in reviewed["files"]:
        assert f["decision"] in {"keep", "merge", "delete"}

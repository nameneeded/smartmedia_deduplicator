import pytest
from src.review.review_logic import add_decision_to_cluster

def test_review_logic_on_sample_cluster():
    cluster = {
        "files": [
            {"path": "/Users/jseanw/Desktop/TRAINING_1-pics/me_and_the_sphinx.jpg", "name": "me_and_the_sphinx.jpg"},
            {"path": "/Users/jseanw/Desktop/TRAINING_1-pics/1000003779 copy.jpg", "name": "1000003779 copy.jpg"},
            {"path": "/Users/jseanw/Desktop/TRAINING_1-pics/1000003779.jpg", "name": "1000003779.jpg"}
        ],
        "weight": 8,
        "index": 1
    }

    # Simulate user decisions
    rotation_map = {
        "/Users/jseanw/Desktop/TRAINING_1-pics/me_and_the_sphinx.jpg": 0,
        "/Users/jseanw/Desktop/TRAINING_1-pics/1000003779 copy.jpg": 0,
        "/Users/jseanw/Desktop/TRAINING_1-pics/1000003779.jpg": 0
    }

    # Inject decisions as if they were selected in the UI
    cluster["files"][0]["decision"] = "keep"
    cluster["files"][1]["decision"] = "delete"
    cluster["files"][2]["decision"] = "keep"

    reviewed = add_decision_to_cluster(
        cluster,
        reviewer="reviewer_name",
        notes="1 line notes",
        rotation_map=rotation_map
    )

    assert reviewed["review"]["summary"] == "dedup"
    assert reviewed["review"]["reviewer"] == "reviewer_name"
    assert reviewed["review"]["notes"] == "1 line notes"

    expected = {
        "me_and_the_sphinx.jpg": "keep",
        "1000003779 copy.jpg": "delete",
        "1000003779.jpg": "keep"
    }

    for f in reviewed["files"]:
        assert f["name"] in expected
        assert f["decision"] == expected[f["name"]]
        assert f["rotation"] == 0
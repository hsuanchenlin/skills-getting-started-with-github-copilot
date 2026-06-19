from src.app import activities


def test_remove_participant_removes_existing_participant(client):
    response = client.delete(
        "/activities/Chess%20Club/participants/michael%40mergington.edu"
    )

    assert response.status_code == 200
    assert response.json() == {
        "message": "Removed michael@mergington.edu from Chess Club"
    }
    assert "michael@mergington.edu" not in activities["Chess Club"]["participants"]


def test_remove_participant_rejects_missing_participant(client):
    response = client.delete(
        "/activities/Chess%20Club/participants/unknown%40mergington.edu"
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Participant not found in this activity"


def test_remove_participant_rejects_missing_activity(client):
    response = client.delete(
        "/activities/Unknown%20Club/participants/unknown%40mergington.edu"
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"
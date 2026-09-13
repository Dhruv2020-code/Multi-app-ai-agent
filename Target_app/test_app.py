from app import process_user_data

def test_process_user_data():
    sample = {"id": 101} # Missing 'email' key
    res = process_user_data(sample)
    assert res["user_id"] == 101
    assert res["email"] is None
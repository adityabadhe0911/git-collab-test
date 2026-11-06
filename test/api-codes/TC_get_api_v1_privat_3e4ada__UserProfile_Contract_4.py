import os
import json
import pytest
import re
import requests

from utilities.fs_data_utility import get_request_data, get_expected_response

BASE_URL = os.getenv("BASE_URL", "")
AUTH_HEADERS = json.loads(os.getenv("AUTH_HEADERS") or "{}")

TEST_CASE_ID = "TC_get_api_v1_privat_3e4ada__UserProfile_Contract_4"


def test_user_profile_schema_conformance():
    """TC_get_api_v1_privat_3e4ada__UserProfile_Contract_4"""
    # Arrange
    request_data = get_request_data(TEST_CASE_ID)
    params = request_data["query_params"]
    json_body = request_data["request_body"]

    # Act
    _output_dir = os.environ.get("OUTPUT_DIR", "./output")
    _headers_dir = os.path.join(_output_dir, "headers")
    os.makedirs(_headers_dir, exist_ok=True)
    try:
        with open(os.path.join(_headers_dir, f"{TEST_CASE_ID}.json"), "w") as _hf:
            json.dump({"test_case_id": TEST_CASE_ID, "headers": AUTH_HEADERS}, _hf, indent=2, default=str)
    except Exception:
        pass

    try:
        response = requests.get(f"{BASE_URL}/api/v1/private/user/profile", headers=AUTH_HEADERS, params=params, json=json_body)
    except requests.exceptions.RequestException as e:
        print(f"[FAIL] {TEST_CASE_ID}: API request failed: {e}")
        pytest.fail(f"API request failed: {e}")

    print(f"[INFO] GET /api/v1/private/user/profile -> {response.status_code}")

    _response_dir = os.path.join(_output_dir, "response_bodies")
    os.makedirs(_response_dir, exist_ok=True)
    try:
        _body_for_report = response.json()
    except Exception:
        _body_for_report = response.text
    try:
        with open(os.path.join(_response_dir, f"{TEST_CASE_ID}.json"), "w") as _rf:
            json.dump({"test_case_id": TEST_CASE_ID, "status_code": response.status_code, "response_body": _body_for_report}, _rf, indent=2, default=str)
    except Exception:
        pass

    # Assert
    expected = get_expected_response(TEST_CASE_ID)
    try:
        assert 200 <= response.status_code < 300
        body = response.json()
        assert response.headers.get("Content-Type") == "application/json"

        # Verify each top-level field is present and matches expected schema
        assert set(body.keys()) == set(expected.keys())

        # id: integer and non-null
        assert isinstance(body["id"], int)
        assert body["id"] == expected["id"]

        # firstName: non-null string
        assert isinstance(body["firstName"], str)
        assert body["firstName"] == expected["firstName"]

        # lastName: non-null string
        assert isinstance(body["lastName"], str)
        assert body["lastName"] == expected["lastName"]

        # emailAddress: non-null string with email format
        assert isinstance(body["emailAddress"], str)
        email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        assert re.match(email_pattern, body["emailAddress"]) is not None
        assert body["emailAddress"] == expected["emailAddress"]

        # defaultLanguage: non-null string
        assert isinstance(body["defaultLanguage"], str)
        assert body["defaultLanguage"] == expected["defaultLanguage"]

        # userName: non-null string
        assert isinstance(body["userName"], str)
        assert body["userName"] == expected["userName"]

        # active: boolean
        assert isinstance(body["active"], bool)
        assert body["active"] == expected["active"]

        # lastAccess: string or null
        assert body.get("lastAccess") is None or isinstance(body["lastAccess"], str)
        assert body.get("lastAccess") == expected.get("lastAccess")

        # loginTime: string or null
        assert body.get("loginTime") is None or isinstance(body["loginTime"], str)
        assert body.get("loginTime") == expected.get("loginTime")

        # merchant: non-null string
        assert isinstance(body["merchant"], str)
        assert body["merchant"] == expected["merchant"]

        # permissions: array of objects with non-null integer id and non-null string name
        assert isinstance(body["permissions"], list)
        assert len(body["permissions"]) == len(expected["permissions"])
        for p, exp in zip(body["permissions"], expected["permissions"]):
            assert isinstance(p, dict)
            assert isinstance(p["id"], int)
            assert isinstance(p["name"], str)
            assert p["id"] == exp["id"]
            assert p["name"] == exp["name"]

        # groups: array of objects with non-null string name, integer id, and nullable type
        assert isinstance(body["groups"], list)
        assert len(body["groups"]) == len(expected["groups"])
        for g, exp in zip(body["groups"], expected["groups"]):
            assert isinstance(g, dict)
            assert isinstance(g["name"], str)
            assert isinstance(g["id"], int)
            assert g.get("type") is None or isinstance(g["type"], str)
            assert g["name"] == exp["name"]
            assert g["id"] == exp["id"]
            assert g.get("type") == exp.get("type")

        print(f"[PASS] {TEST_CASE_ID}: all assertions passed (status={response.status_code})")
    except AssertionError as e:
        print(f"[FAIL] {TEST_CASE_ID}: {e}")
        raise

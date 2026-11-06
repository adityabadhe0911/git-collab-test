import os
import json
import pytest
import requests

from utilities.fs_data_utility import get_request_data, get_expected_response

BASE_URL = os.getenv("BASE_URL", "")
AUTH_HEADERS = json.loads(os.getenv("AUTH_HEADERS") or "{}")

TEST_CASE_ID = "TC_get_api_v1_privat_3e4ada__UserProfile_Neg_MissingAuth_3"


def test_get_user_profile_missing_auth():
    """TC_get_api_v1_privat_3e4ada__UserProfile_Neg_MissingAuth_3"""
    # Arrange
    request_data = get_request_data(TEST_CASE_ID)
    params = request_data["query_params"]
    json_body = request_data["request_body"]

    # Build headers explicitly without Authorization for this negative test
    headers = {}

    # Act
    _output_dir = os.environ.get("OUTPUT_DIR", "./output")
    _headers_dir = os.path.join(_output_dir, "headers")
    os.makedirs(_headers_dir, exist_ok=True)
    try:
        with open(os.path.join(_headers_dir, f"{TEST_CASE_ID}.json"), "w") as _hf:
            json.dump({"test_case_id": TEST_CASE_ID, "headers": headers}, _hf, indent=2, default=str)
    except Exception:
        pass

    try:
        response = requests.get(f"{BASE_URL}/api/v1/private/user/profile", headers=headers, params=params, json=json_body)
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
        assert response.status_code == 401
        body = response.json()

        # Verify response Content-Type header is application/json
        assert response.headers.get("Content-Type") == "application/json"

        # Verify response body's `status` field equals 401
        assert isinstance(body["status"], int)
        assert body["status"] == 401

        # Verify response body's `error` field is a non-empty descriptive string
        assert isinstance(body["error"], str)
        assert body["error"]

        # Verify response body's `path` field matches the requested endpoint path
        assert isinstance(body["path"], str)
        assert body["path"] == "/api/v1/private/user/profile"

        # Verify no user profile data is present in the response
        # The error response body should only contain timestamp, status, error, path
        assert "id" not in body
        assert "userName" not in body
        assert "emailAddress" not in body
        assert "firstName" not in body
        assert "lastName" not in body
        assert "active" not in body
        assert "defaultLanguage" not in body
        assert "merchant" not in body
        assert "lastAccess" not in body
        assert "loginTime" not in body
        assert "groups" not in body
        assert "permissions" not in body

        print(f"[PASS] {TEST_CASE_ID}: all assertions passed (status={response.status_code})")
    except AssertionError as e:
        print(f"[FAIL] {TEST_CASE_ID}: {e}")
        raise

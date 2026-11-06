import os
import json
import pytest
import requests

from utilities.fs_data_utility import get_request_data, get_expected_response

BASE_URL = os.getenv("BASE_URL", "")
AUTH_HEADERS = json.loads(os.getenv("AUTH_HEADERS") or "{}")

TEST_CASE_ID = "TC_get_api_v1_privat_3e4ada__UserProfile_Pos_NoLang_1"


def test_get_user_profile_with_valid_jwt_no_lang():
    """TC_get_api_v1_privat_3e4ada__UserProfile_Pos_NoLang_1"""
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
        assert response.status_code == 200
        body = response.json()

        # Verify response Content-Type header is application/json
        assert response.headers.get("Content-Type") == "application/json"

        # Verify response body is valid, well-formed JSON
        assert isinstance(body, dict)

        # Verify each top-level field is present and matches its declared type and nullability
        # id: integer, nullable: false
        assert "id" in body
        assert isinstance(body["id"], int)
        assert body["id"] == expected["id"]

        # firstName: string, nullable: false
        assert "firstName" in body
        assert isinstance(body["firstName"], str)
        assert body["firstName"] == expected["firstName"]

        # lastName: string, nullable: false
        assert "lastName" in body
        assert isinstance(body["lastName"], str)
        assert body["lastName"] == expected["lastName"]

        # emailAddress: string, format: email, nullable: false
        assert "emailAddress" in body
        assert isinstance(body["emailAddress"], str)
        assert body["emailAddress"] == expected["emailAddress"]

        # defaultLanguage: string, nullable: false
        assert "defaultLanguage" in body
        assert isinstance(body["defaultLanguage"], str)
        assert body["defaultLanguage"] == expected["defaultLanguage"]

        # userName: string, nullable: false
        assert "userName" in body
        assert isinstance(body["userName"], str)
        assert body["userName"] == expected["userName"]

        # active: boolean, nullable: false
        assert "active" in body
        assert isinstance(body["active"], bool)
        assert body["active"] == expected["active"]

        # lastAccess: string, nullable: true
        assert "lastAccess" in body
        assert body["lastAccess"] is None or isinstance(body["lastAccess"], str)
        assert body["lastAccess"] == expected.get("lastAccess")

        # loginTime: string, nullable: true
        assert "loginTime" in body
        assert body["loginTime"] is None or isinstance(body["loginTime"], str)
        assert body["loginTime"] == expected.get("loginTime")

        # merchant: string, nullable: false
        assert "merchant" in body
        assert isinstance(body["merchant"], str)
        assert body["merchant"] == expected["merchant"]

        # permissions: array of objects with id (integer) and name (string), nullable: false
        assert "permissions" in body
        assert isinstance(body["permissions"], list)
        assert len(body["permissions"]) == len(expected["permissions"])
        for i, perm in enumerate(body["permissions"]):
            assert isinstance(perm, dict)
            assert "id" in perm
            assert isinstance(perm["id"], int)
            assert perm["id"] == expected["permissions"][i]["id"]
            assert "name" in perm
            assert isinstance(perm["name"], str)
            assert perm["name"] == expected["permissions"][i]["name"]
        assert body["permissions"] == expected["permissions"]

        # groups: array of objects with name (string), type (string, nullable), id (integer), nullable: false
        assert "groups" in body
        assert isinstance(body["groups"], list)
        assert len(body["groups"]) == len(expected["groups"])
        for i, group in enumerate(body["groups"]):
            assert isinstance(group, dict)
            assert "name" in group
            assert isinstance(group["name"], str)
            assert group["name"] == expected["groups"][i]["name"]
            assert "type" in group
            assert group["type"] is None or isinstance(group["type"], str)
            assert group["type"] == expected["groups"][i].get("type")
            assert "id" in group
            assert isinstance(group["id"], int)
            assert group["id"] == expected["groups"][i]["id"]
        assert body["groups"] == expected["groups"]

        # Verify no additional top-level fields are present beyond those defined in the schema
        expected_fields = {"id", "firstName", "lastName", "emailAddress", "defaultLanguage", "userName", "active", "lastAccess", "loginTime", "merchant", "permissions", "groups"}
        assert set(body.keys()) == expected_fields

        print(f"[PASS] {TEST_CASE_ID}: all assertions passed (status={response.status_code})")
    except AssertionError as e:
        print(f"[FAIL] {TEST_CASE_ID}: {e}")
        raise

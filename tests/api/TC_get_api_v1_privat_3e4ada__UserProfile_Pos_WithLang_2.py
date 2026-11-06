import os
import json
import pytest
import requests

from utilities.fs_data_utility import get_request_data, get_expected_response

BASE_URL = os.getenv("BASE_URL", "")
AUTH_HEADERS = json.loads(os.getenv("AUTH_HEADERS") or "{}")

TEST_CASE_ID = "TC_get_api_v1_privat_3e4ada__UserProfile_Pos_WithLang_2"


def test_get_user_profile_with_lang_param():
    """TC_get_api_v1_privat_3e4ada__UserProfile_Pos_WithLang_2"""
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
        assert 200 <= response.status_code < 300, f"Expected status code in 2XX range, got {response.status_code}"
        body = response.json()
        
        # Verify Content-Type header is application/json
        assert response.headers.get("Content-Type") == "application/json", f"Expected Content-Type to be 'application/json', got '{response.headers.get('Content-Type')}'"
        
        # Verify response body is valid JSON (already done by response.json() above)
        
        # Verify all required fields and their types
        assert isinstance(body.get("id"), int), f"Expected 'id' to be an integer, got {type(body.get('id'))}"
        assert isinstance(body.get("firstName"), str), f"Expected 'firstName' to be a string, got {type(body.get('firstName'))}"
        assert isinstance(body.get("lastName"), str), f"Expected 'lastName' to be a string, got {type(body.get('lastName'))}"
        assert isinstance(body.get("emailAddress"), str), f"Expected 'emailAddress' to be a string, got {type(body.get('emailAddress'))}"
        assert isinstance(body.get("defaultLanguage"), str), f"Expected 'defaultLanguage' to be a string, got {type(body.get('defaultLanguage'))}"
        assert isinstance(body.get("userName"), str), f"Expected 'userName' to be a string, got {type(body.get('userName'))}"
        assert isinstance(body.get("active"), bool), f"Expected 'active' to be a boolean, got {type(body.get('active'))}"
        
        # Verify nullable fields
        if body.get("lastAccess") is not None:
            assert isinstance(body.get("lastAccess"), str), f"Expected 'lastAccess' to be a string or null, got {type(body.get('lastAccess'))}"
        if body.get("loginTime") is not None:
            assert isinstance(body.get("loginTime"), str), f"Expected 'loginTime' to be a string or null, got {type(body.get('loginTime'))}"
        
        assert isinstance(body.get("merchant"), str), f"Expected 'merchant' to be a string, got {type(body.get('merchant'))}"
        
        # Verify arrays
        assert isinstance(body.get("permissions"), list), f"Expected 'permissions' to be a list, got {type(body.get('permissions'))}"
        assert isinstance(body.get("groups"), list), f"Expected 'groups' to be a list, got {type(body.get('groups'))}"
        
        # Verify email format for emailAddress
        import re
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        assert re.match(email_pattern, body.get("emailAddress", "")), f"Expected 'emailAddress' to be a valid email format"
        
        # Verify id is positive integer
        assert body.get("id") > 0, f"Expected 'id' to be a positive integer, got {body.get('id')}"
        
        # Verify defaultLanguage matches the lang parameter from the request
        expected_lang = expected.get("defaultLanguage")
        actual_lang = body.get("defaultLanguage")
        assert actual_lang == expected_lang, f"Expected 'defaultLanguage' to be '{expected_lang}', got '{actual_lang}'"
        
        # Verify all other fields conform to their declared types and nullability (exact-value comparison for 2XX)
        assert body.get("id") == expected.get("id"), f"Expected 'id' to be {expected.get('id')}, got {body.get('id')}"
        assert body.get("firstName") == expected.get("firstName"), f"Expected 'firstName' to be '{expected.get('firstName')}', got '{body.get('firstName')}'"
        assert body.get("lastName") == expected.get("lastName"), f"Expected 'lastName' to be '{expected.get('lastName')}', got '{body.get('lastName')}'"
        assert body.get("emailAddress") == expected.get("emailAddress"), f"Expected 'emailAddress' to be '{expected.get('emailAddress')}', got '{body.get('emailAddress')}'"
        assert body.get("userName") == expected.get("userName"), f"Expected 'userName' to be '{expected.get('userName')}', got '{body.get('userName')}'"
        assert body.get("active") == expected.get("active"), f"Expected 'active' to be {expected.get('active')}, got {body.get('active')}"
        
        # Verify nullable fields match expected values
        if expected.get("lastAccess") is not None:
            assert body.get("lastAccess") == expected.get("lastAccess"), f"Expected 'lastAccess' to be '{expected.get('lastAccess')}', got '{body.get('lastAccess')}'"
        else:
            assert body.get("lastAccess") is None, f"Expected 'lastAccess' to be null, got '{body.get('lastAccess')}'"
        
        if expected.get("loginTime") is not None:
            assert body.get("loginTime") == expected.get("loginTime"), f"Expected 'loginTime' to be '{expected.get('loginTime')}', got '{body.get('loginTime')}'"
        else:
            assert body.get("loginTime") is None, f"Expected 'loginTime' to be null, got '{body.get('loginTime')}'"
        
        assert body.get("merchant") == expected.get("merchant"), f"Expected 'merchant' to be '{expected.get('merchant')}', got '{body.get('merchant')}'"
        
        # Verify permissions array
        assert len(body.get("permissions", [])) == len(expected.get("permissions", [])), f"Expected 'permissions' to have {len(expected.get('permissions', []))} items, got {len(body.get('permissions', []))}"
        for i, (actual_perm, expected_perm) in enumerate(zip(body.get("permissions", []), expected.get("permissions", []))):
            assert isinstance(actual_perm.get("id"), int), f"Expected 'permissions[{i}].id' to be an integer, got {type(actual_perm.get('id'))}"
            assert isinstance(actual_perm.get("name"), str), f"Expected 'permissions[{i}].name' to be a string, got {type(actual_perm.get('name'))}"
            assert actual_perm.get("id") == expected_perm.get("id"), f"Expected 'permissions[{i}].id' to be {expected_perm.get('id')}, got {actual_perm.get('id')}"
            assert actual_perm.get("name") == expected_perm.get("name"), f"Expected 'permissions[{i}].name' to be '{expected_perm.get('name')}', got '{actual_perm.get('name')}'"
        
        # Verify groups array
        assert len(body.get("groups", [])) == len(expected.get("groups", [])), f"Expected 'groups' to have {len(expected.get('groups', []))} items, got {len(body.get('groups', []))}"
        for i, (actual_group, expected_group) in enumerate(zip(body.get("groups", []), expected.get("groups", []))):
            assert isinstance(actual_group.get("name"), str), f"Expected 'groups[{i}].name' to be a string, got {type(actual_group.get('name'))}"
            if actual_group.get("type") is not None:
                assert isinstance(actual_group.get("type"), str), f"Expected 'groups[{i}].type' to be a string or null, got {type(actual_group.get('type'))}"
            assert isinstance(actual_group.get("id"), int), f"Expected 'groups[{i}].id' to be an integer, got {type(actual_group.get('id'))}"
            assert actual_group.get("name") == expected_group.get("name"), f"Expected 'groups[{i}].name' to be '{expected_group.get('name')}', got '{actual_group.get('name')}'"
            if expected_group.get("type") is not None:
                assert actual_group.get("type") == expected_group.get("type"), f"Expected 'groups[{i}].type' to be '{expected_group.get('type')}', got '{actual_group.get('type')}'"
            assert actual_group.get("id") == expected_group.get("id"), f"Expected 'groups[{i}].id' to be {expected_group.get('id')}, got {actual_group.get('id')}"
        
        print(f"[PASS] {TEST_CASE_ID}: all assertions passed (status={response.status_code})")
    except AssertionError as e:
        print(f"[FAIL] {TEST_CASE_ID}: {e}")
        raise

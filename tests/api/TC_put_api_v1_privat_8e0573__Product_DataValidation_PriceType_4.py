import os
import json
import pytest
import requests

from utilities.fs_data_utility import get_request_data, get_expected_response

BASE_URL = os.getenv("BASE_URL", "")
AUTH_HEADERS = json.loads(os.getenv("AUTH_HEADERS") or "{}")

TEST_CASE_ID = "TC_put_api_v1_privat_8e0573__Product_DataValidation_PriceType_4"


def test_put_product_price_validation_error():
    """TC_put_api_v1_privat_8e0573__Product_DataValidation_PriceType_4"""
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
        response = requests.put(f"{BASE_URL}/api/v1/private/product/{request_data['path_params']['id']}", headers=AUTH_HEADERS, params=params, json=json_body)
    except requests.exceptions.RequestException as e:
        print(f"[FAIL] {TEST_CASE_ID}: API request failed: {e}")
        pytest.fail(f"API request failed: {e}")

    print(f"[INFO] PUT /api/v1/private/product/{{id}} -> {response.status_code}")

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
        assert response.status_code == 400
        body = response.json()
        assert isinstance(body["status"], int)
        assert body["status"] == 400
        assert isinstance(body["error"], str)
        assert "type mismatch" in body["error"].lower() and "price" in body["error"].lower()
        assert isinstance(body["timestamp"], str)
        assert isinstance(body["path"], str)
        print(f"[PASS] {TEST_CASE_ID}: all assertions passed (status={response.status_code})")
    except AssertionError as e:
        print(f"[FAIL] {TEST_CASE_ID}: {e}")
        raise

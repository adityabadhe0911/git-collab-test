import os
import json
import pytest
import requests

from utilities.fs_data_utility import get_request_data, get_expected_response

BASE_URL = os.getenv("BASE_URL", "")
AUTH_HEADERS = json.loads(os.getenv("AUTH_HEADERS") or "{}")

TEST_CASE_ID = "TC_put_api_v1_privat_8e0573__Product_Positive_NoQuery_1"


def test_update_product_with_valid_id_and_complete_body():
    """TC_put_api_v1_privat_8e0573__Product_Positive_NoQuery_1"""
    # Arrange
    request_data = get_request_data(TEST_CASE_ID)
    params = request_data["query_params"]
    json_body = request_data["request_body"]
    path_params = request_data["path_params"]
    
    # Build the path with the product ID
    product_id = path_params["id"]
    path = f"/api/v1/private/product/{product_id}"

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
        response = requests.put(f"{BASE_URL}{path}", headers=AUTH_HEADERS, params=params, json=json_body)
    except requests.exceptions.RequestException as e:
        print(f"[FAIL] {TEST_CASE_ID}: API request failed: {e}")
        pytest.fail(f"API request failed: {e}")

    print(f"[INFO] put {path} -> {response.status_code}")

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
        
        # Verify Content-Type header
        assert response.headers.get("Content-Type") == "application/json"
        
        # Verify response body is valid JSON (already parsed above)
        assert isinstance(body, dict)
        
        # Assert all required fields with type checks and exact value comparison
        assert "id" in body
        assert isinstance(body["id"], int)
        assert body["id"] == expected["id"]
        assert body["id"] == product_id
        
        assert "sku" in body
        assert isinstance(body["sku"], str)
        assert body["sku"] == expected["sku"]
        
        assert "refSku" in body
        assert isinstance(body["refSku"], str)
        assert body["refSku"] == expected["refSku"]
        
        assert "price" in body
        assert isinstance(body["price"], (int, float))
        assert body["price"] == expected["price"]
        
        assert "quantity" in body
        assert isinstance(body["quantity"], int)
        assert body["quantity"] == expected["quantity"]
        
        assert "available" in body
        assert isinstance(body["available"], bool)
        assert body["available"] == expected["available"]
        
        assert "visible" in body
        assert isinstance(body["visible"], bool)
        assert body["visible"] == expected["visible"]
        
        assert "productShipeable" in body
        assert isinstance(body["productShipeable"], bool)
        assert body["productShipeable"] == expected["productShipeable"]
        
        assert "productVirtual" in body
        assert isinstance(body["productVirtual"], bool)
        assert body["productVirtual"] == expected["productVirtual"]
        
        assert "preOrder" in body
        assert isinstance(body["preOrder"], bool)
        assert body["preOrder"] == expected["preOrder"]
        
        assert "productIsFree" in body
        assert isinstance(body["productIsFree"], bool)
        assert body["productIsFree"] == expected["productIsFree"]
        
        assert "quantityOrderMinimum" in body
        assert isinstance(body["quantityOrderMinimum"], int)
        assert body["quantityOrderMinimum"] == expected["quantityOrderMinimum"]
        
        assert "quantityOrderMaximum" in body
        assert isinstance(body["quantityOrderMaximum"], int)
        assert body["quantityOrderMaximum"] == expected["quantityOrderMaximum"]
        
        assert "sortOrder" in body
        assert isinstance(body["sortOrder"], int)
        assert body["sortOrder"] == expected["sortOrder"]
        
        assert "dateAvailable" in body
        assert isinstance(body["dateAvailable"], str)
        assert body["dateAvailable"] == expected["dateAvailable"]
        
        # creationDate is nullable
        assert "creationDate" in body
        if expected.get("creationDate") is None:
            assert body.get("creationDate") is None
        else:
            assert isinstance(body["creationDate"], str)
            assert body["creationDate"] == expected["creationDate"]
        
        assert "rating" in body
        assert isinstance(body["rating"], (int, float))
        assert body["rating"] == expected["rating"]
        
        assert "ratingCount" in body
        assert isinstance(body["ratingCount"], int)
        assert body["ratingCount"] == expected["ratingCount"]
        
        assert "rentalDuration" in body
        assert isinstance(body["rentalDuration"], int)
        assert body["rentalDuration"] == expected["rentalDuration"]
        
        assert "rentalPeriod" in body
        assert isinstance(body["rentalPeriod"], int)
        assert body["rentalPeriod"] == expected["rentalPeriod"]
        
        # type is nullable
        assert "type" in body
        if expected.get("type") is None:
            assert body.get("type") is None
        else:
            assert isinstance(body["type"], str)
            assert body["type"] == expected["type"]
        
        # descriptions array
        assert "descriptions" in body
        assert isinstance(body["descriptions"], list)
        assert body["descriptions"] == expected["descriptions"]
        
        # categories array
        assert "categories" in body
        assert isinstance(body["categories"], list)
        assert body["categories"] == expected["categories"]
        
        # productSpecifications object
        assert "productSpecifications" in body
        assert isinstance(body["productSpecifications"], dict)
        assert body["productSpecifications"] == expected["productSpecifications"]
        
        # attributes is nullable
        assert "attributes" in body
        if expected.get("attributes") is None:
            assert body.get("attributes") is None
        else:
            assert isinstance(body["attributes"], list)
            assert body["attributes"] == expected["attributes"]
        
        # images is nullable
        assert "images" in body
        if expected.get("images") is None:
            assert body.get("images") is None
        else:
            assert isinstance(body["images"], list)
            assert body["images"] == expected["images"]
        
        # productPrices is nullable
        assert "productPrices" in body
        if expected.get("productPrices") is None:
            assert body.get("productPrices") is None
        else:
            assert isinstance(body["productPrices"], list)
            assert body["productPrices"] == expected["productPrices"]
        
        # relatedProducts is nullable
        assert "relatedProducts" in body
        if expected.get("relatedProducts") is None:
            assert body.get("relatedProducts") is None
        else:
            assert isinstance(body["relatedProducts"], list)
            assert body["relatedProducts"] == expected["relatedProducts"]
        
        # owner object
        assert "owner" in body
        assert isinstance(body["owner"], dict)
        assert body["owner"] == expected["owner"]
        
        print(f"[PASS] {TEST_CASE_ID}: all assertions passed (status={response.status_code})")
    except AssertionError as e:
        print(f"[FAIL] {TEST_CASE_ID}: {e}")
        raise

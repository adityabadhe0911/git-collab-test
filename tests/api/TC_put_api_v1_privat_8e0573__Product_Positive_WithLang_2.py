import os
import json
import pytest
import requests

from utilities.fs_data_utility import get_request_data, get_expected_response

BASE_URL = os.getenv("BASE_URL", "")
AUTH_HEADERS = json.loads(os.getenv("AUTH_HEADERS") or "{}")

TEST_CASE_ID = "TC_put_api_v1_privat_8e0573__Product_Positive_WithLang_2"


def test_update_product_with_lang_localization():
    """TC_put_api_v1_privat_8e0573__Product_Positive_WithLang_2"""
    # Arrange
    request_data = get_request_data(TEST_CASE_ID)
    path_params = request_data["path_params"]
    query_params = request_data["query_params"]
    json_body = request_data["request_body"]

    # Build the path with the product ID
    product_id = path_params["id"]
    endpoint_path = f"/api/v1/private/product/{product_id}"

    # Build headers with Authorization and Content-Type
    headers = {**AUTH_HEADERS, "Content-Type": "application/json"}

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
        response = requests.put(f"{BASE_URL}{endpoint_path}", headers=headers, params=query_params, json=json_body)
    except requests.exceptions.RequestException as e:
        print(f"[FAIL] {TEST_CASE_ID}: API request failed: {e}")
        pytest.fail(f"API request failed: {e}")

    print(f"[INFO] put {endpoint_path} -> {response.status_code}")

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
        # Status code in 2XX range
        assert 200 <= response.status_code < 300
        
        # Content-Type header verification
        assert response.headers.get("Content-Type") == "application/json"
        
        body = response.json()
        
        # Assert all required fields with type and exact value comparison
        # id field
        assert "id" in body
        assert isinstance(body["id"], int)
        assert body["id"] == expected["id"]
        # Verify id matches path parameter
        assert body["id"] == int(product_id)
        
        # sku field
        assert "sku" in body
        assert isinstance(body["sku"], str)
        assert body["sku"] == expected["sku"]
        
        # refSku field
        assert "refSku" in body
        assert isinstance(body["refSku"], str)
        assert body["refSku"] == expected["refSku"]
        
        # price field
        assert "price" in body
        assert isinstance(body["price"], (int, float))
        assert body["price"] == expected["price"]
        
        # quantity field
        assert "quantity" in body
        assert isinstance(body["quantity"], int)
        assert body["quantity"] == expected["quantity"]
        
        # available field
        assert "available" in body
        assert isinstance(body["available"], bool)
        assert body["available"] == expected["available"]
        
        # visible field
        assert "visible" in body
        assert isinstance(body["visible"], bool)
        assert body["visible"] == expected["visible"]
        
        # productShipeable field
        assert "productShipeable" in body
        assert isinstance(body["productShipeable"], bool)
        assert body["productShipeable"] == expected["productShipeable"]
        
        # productVirtual field
        assert "productVirtual" in body
        assert isinstance(body["productVirtual"], bool)
        assert body["productVirtual"] == expected["productVirtual"]
        
        # preOrder field
        assert "preOrder" in body
        assert isinstance(body["preOrder"], bool)
        assert body["preOrder"] == expected["preOrder"]
        
        # productIsFree field
        assert "productIsFree" in body
        assert isinstance(body["productIsFree"], bool)
        assert body["productIsFree"] == expected["productIsFree"]
        
        # quantityOrderMinimum field
        assert "quantityOrderMinimum" in body
        assert isinstance(body["quantityOrderMinimum"], int)
        assert body["quantityOrderMinimum"] == expected["quantityOrderMinimum"]
        
        # quantityOrderMaximum field
        assert "quantityOrderMaximum" in body
        assert isinstance(body["quantityOrderMaximum"], int)
        assert body["quantityOrderMaximum"] == expected["quantityOrderMaximum"]
        
        # sortOrder field
        assert "sortOrder" in body
        assert isinstance(body["sortOrder"], int)
        assert body["sortOrder"] == expected["sortOrder"]
        
        # dateAvailable field
        assert "dateAvailable" in body
        assert isinstance(body["dateAvailable"], str)
        assert body["dateAvailable"] == expected["dateAvailable"]
        
        # creationDate field (nullable)
        assert "creationDate" in body
        if expected.get("creationDate") is None:
            assert body.get("creationDate") is None
        else:
            assert isinstance(body["creationDate"], str)
            assert body["creationDate"] == expected["creationDate"]
        
        # rating field
        assert "rating" in body
        assert isinstance(body["rating"], (int, float))
        assert body["rating"] == expected["rating"]
        
        # ratingCount field
        assert "ratingCount" in body
        assert isinstance(body["ratingCount"], int)
        assert body["ratingCount"] == expected["ratingCount"]
        
        # rentalDuration field
        assert "rentalDuration" in body
        assert isinstance(body["rentalDuration"], int)
        assert body["rentalDuration"] == expected["rentalDuration"]
        
        # rentalPeriod field
        assert "rentalPeriod" in body
        assert isinstance(body["rentalPeriod"], int)
        assert body["rentalPeriod"] == expected["rentalPeriod"]
        
        # type field (nullable)
        assert "type" in body
        if expected.get("type") is None:
            assert body.get("type") is None
        else:
            assert isinstance(body["type"], str)
            assert body["type"] == expected["type"]
        
        # descriptions field (array of ProductDescription)
        assert "descriptions" in body
        assert isinstance(body["descriptions"], list)
        assert len(body["descriptions"]) == len(expected["descriptions"])
        # Verify localized fields are in requested language
        for i, desc in enumerate(body["descriptions"]):
            assert isinstance(desc, dict)
            # Check that the description contains the language parameter value
            if query_params and "lang" in query_params:
                expected_lang = query_params["lang"]
                # The descriptions should be localized to the requested language
                # This is verified by checking the language field in each description
                if "language" in desc:
                    assert desc["language"] == expected_lang
        
        # Compare descriptions against expected
        for i, expected_desc in enumerate(expected["descriptions"]):
            for field in expected_desc:
                assert field in body["descriptions"][i]
                if isinstance(expected_desc[field], str):
                    assert body["descriptions"][i][field] == expected_desc[field]
                elif isinstance(expected_desc[field], list):
                    assert body["descriptions"][i][field] == expected_desc[field]
        
        # categories field (array of Category)
        assert "categories" in body
        assert isinstance(body["categories"], list)
        assert len(body["categories"]) == len(expected["categories"])
        for i, cat in enumerate(body["categories"]):
            assert isinstance(cat, dict)
            for field in expected["categories"][i]:
                assert field in cat
                if isinstance(expected["categories"][i][field], (str, int, float, bool, type(None))):
                    assert cat[field] == expected["categories"][i][field]
        
        # productSpecifications field
        assert "productSpecifications" in body
        assert isinstance(body["productSpecifications"], dict)
        for field in expected["productSpecifications"]:
            assert field in body["productSpecifications"]
            assert body["productSpecifications"][field] == expected["productSpecifications"][field]
        
        # attributes field (nullable array)
        if "attributes" in body:
            assert isinstance(body["attributes"], list)
            if expected.get("attributes") is not None:
                assert len(body["attributes"]) == len(expected["attributes"])
                for i, attr in enumerate(body["attributes"]):
                    assert isinstance(attr, dict)
                    for field in expected["attributes"][i]:
                        assert field in attr
                        if isinstance(expected["attributes"][i][field], (str, int, float, bool, type(None))):
                            assert attr[field] == expected["attributes"][i][field]
        
        # images field (nullable array)
        if "images" in body:
            assert isinstance(body["images"], list)
            if expected.get("images") is not None:
                assert len(body["images"]) == len(expected["images"])
                for i, img in enumerate(body["images"]):
                    assert isinstance(img, dict)
                    for field in expected["images"][i]:
                        assert field in img
                        if isinstance(expected["images"][i][field], (str, int, float, bool, type(None))):
                            assert img[field] == expected["images"][i][field]
        
        # productPrices field (nullable array)
        if "productPrices" in body:
            assert isinstance(body["productPrices"], list)
            if expected.get("productPrices") is not None:
                assert len(body["productPrices"]) == len(expected["productPrices"])
                for i, price in enumerate(body["productPrices"]):
                    assert isinstance(price, dict)
                    for field in expected["productPrices"][i]:
                        assert field in price
                        if isinstance(expected["productPrices"][i][field], (str, int, float, bool, type(None))):
                            assert price[field] == expected["productPrices"][i][field]
        
        # relatedProducts field (nullable array)
        if "relatedProducts" in body:
            assert isinstance(body["relatedProducts"], list)
            if expected.get("relatedProducts") is not None:
                assert len(body["relatedProducts"]) == len(expected["relatedProducts"])
                for i, rel in enumerate(body["relatedProducts"]):
                    assert isinstance(rel, dict)
                    for field in expected["relatedProducts"][i]:
                        assert field in rel
                        if isinstance(expected["relatedProducts"][i][field], (str, int, float, bool, type(None))):
                            assert rel[field] == expected["relatedProducts"][i][field]
        
        # owner field
        assert "owner" in body
        assert isinstance(body["owner"], dict)
        for field in expected["owner"]:
            assert field in body["owner"]
            if isinstance(expected["owner"][field], (str, int, float, bool, type(None))):
                assert body["owner"][field] == expected["owner"][field]
        
        print(f"[PASS] {TEST_CASE_ID}: all assertions passed (status={response.status_code})")
    except AssertionError as e:
        print(f"[FAIL] {TEST_CASE_ID}: {e}")
        raise

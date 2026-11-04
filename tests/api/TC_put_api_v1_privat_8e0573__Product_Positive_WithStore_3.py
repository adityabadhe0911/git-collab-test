import os
import json
import pytest
import requests

from utilities.fs_data_utility import get_request_data, get_expected_response

BASE_URL = os.getenv("BASE_URL", "")
AUTH_HEADERS = json.loads(os.getenv("AUTH_HEADERS") or "{}")

TEST_CASE_ID = "TC_put_api_v1_privat_8e0573__Product_Positive_WithStore_3"


def test_update_product_with_store_scoping():
    """TC_put_api_v1_privat_8e0573__Product_Positive_WithStore_3"""
    # Arrange
    request_data = get_request_data(TEST_CASE_ID)
    path_params = request_data["path_params"]
    query_params = request_data["query_params"]
    json_body = request_data["request_body"]

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
        response = requests.put(f"{BASE_URL}{path}", headers=AUTH_HEADERS, params=query_params, json=json_body)
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
        assert 200 <= response.status_code < 300, f"Expected 2XX status, got {response.status_code}"
        body = response.json()
        
        # Verify Content-Type header is application/json
        assert response.headers.get("Content-Type") == "application/json", f"Expected Content-Type application/json, got {response.headers.get('Content-Type')}"
        
        # Verify all response fields match expected schema and values
        # id: integer (int64), not nullable
        assert "id" in body, "Response body missing 'id' field"
        assert isinstance(body["id"], int), f"Expected id to be int, got {type(body['id'])}"
        assert body["id"] == expected["id"], f"Expected id {expected['id']}, got {body['id']}"
        
        # sku: string, not nullable
        assert "sku" in body, "Response body missing 'sku' field"
        assert isinstance(body["sku"], str), f"Expected sku to be str, got {type(body['sku'])}"
        assert body["sku"] == expected["sku"], f"Expected sku {expected['sku']}, got {body['sku']}"
        
        # refSku: string, not nullable
        assert "refSku" in body, "Response body missing 'refSku' field"
        assert isinstance(body["refSku"], str), f"Expected refSku to be str, got {type(body['refSku'])}"
        assert body["refSku"] == expected["refSku"], f"Expected refSku {expected['refSku']}, got {body['refSku']}"
        
        # price: number, not nullable
        assert "price" in body, "Response body missing 'price' field"
        assert isinstance(body["price"], (int, float)), f"Expected price to be number, got {type(body['price'])}"
        assert body["price"] == expected["price"], f"Expected price {expected['price']}, got {body['price']}"
        
        # quantity: integer (int32), not nullable
        assert "quantity" in body, "Response body missing 'quantity' field"
        assert isinstance(body["quantity"], int), f"Expected quantity to be int, got {type(body['quantity'])}"
        assert body["quantity"] == expected["quantity"], f"Expected quantity {expected['quantity']}, got {body['quantity']}"
        
        # available: boolean, not nullable
        assert "available" in body, "Response body missing 'available' field"
        assert isinstance(body["available"], bool), f"Expected available to be bool, got {type(body['available'])}"
        assert body["available"] == expected["available"], f"Expected available {expected['available']}, got {body['available']}"
        
        # visible: boolean, not nullable
        assert "visible" in body, "Response body missing 'visible' field"
        assert isinstance(body["visible"], bool), f"Expected visible to be bool, got {type(body['visible'])}"
        assert body["visible"] == expected["visible"], f"Expected visible {expected['visible']}, got {body['visible']}"
        
        # productShipeable: boolean, not nullable
        assert "productShipeable" in body, "Response body missing 'productShipeable' field"
        assert isinstance(body["productShipeable"], bool), f"Expected productShipeable to be bool, got {type(body['productShipeable'])}"
        assert body["productShipeable"] == expected["productShipeable"], f"Expected productShipeable {expected['productShipeable']}, got {body['productShipeable']}"
        
        # productVirtual: boolean, not nullable
        assert "productVirtual" in body, "Response body missing 'productVirtual' field"
        assert isinstance(body["productVirtual"], bool), f"Expected productVirtual to be bool, got {type(body['productVirtual'])}"
        assert body["productVirtual"] == expected["productVirtual"], f"Expected productVirtual {expected['productVirtual']}, got {body['productVirtual']}"
        
        # preOrder: boolean, not nullable
        assert "preOrder" in body, "Response body missing 'preOrder' field"
        assert isinstance(body["preOrder"], bool), f"Expected preOrder to be bool, got {type(body['preOrder'])}"
        assert body["preOrder"] == expected["preOrder"], f"Expected preOrder {expected['preOrder']}, got {body['preOrder']}"
        
        # productIsFree: boolean, not nullable
        assert "productIsFree" in body, "Response body missing 'productIsFree' field"
        assert isinstance(body["productIsFree"], bool), f"Expected productIsFree to be bool, got {type(body['productIsFree'])}"
        assert body["productIsFree"] == expected["productIsFree"], f"Expected productIsFree {expected['productIsFree']}, got {body['productIsFree']}"
        
        # quantityOrderMinimum: integer (int32), not nullable
        assert "quantityOrderMinimum" in body, "Response body missing 'quantityOrderMinimum' field"
        assert isinstance(body["quantityOrderMinimum"], int), f"Expected quantityOrderMinimum to be int, got {type(body['quantityOrderMinimum'])}"
        assert body["quantityOrderMinimum"] == expected["quantityOrderMinimum"], f"Expected quantityOrderMinimum {expected['quantityOrderMinimum']}, got {body['quantityOrderMinimum']}"
        
        # quantityOrderMaximum: integer (int32), not nullable
        assert "quantityOrderMaximum" in body, "Response body missing 'quantityOrderMaximum' field"
        assert isinstance(body["quantityOrderMaximum"], int), f"Expected quantityOrderMaximum to be int, got {type(body['quantityOrderMaximum'])}"
        assert body["quantityOrderMaximum"] == expected["quantityOrderMaximum"], f"Expected quantityOrderMaximum {expected['quantityOrderMaximum']}, got {body['quantityOrderMaximum']}"
        
        # sortOrder: integer (int32), not nullable
        assert "sortOrder" in body, "Response body missing 'sortOrder' field"
        assert isinstance(body["sortOrder"], int), f"Expected sortOrder to be int, got {type(body['sortOrder'])}"
        assert body["sortOrder"] == expected["sortOrder"], f"Expected sortOrder {expected['sortOrder']}, got {body['sortOrder']}"
        
        # dateAvailable: string (date), not nullable
        assert "dateAvailable" in body, "Response body missing 'dateAvailable' field"
        assert isinstance(body["dateAvailable"], str), f"Expected dateAvailable to be str, got {type(body['dateAvailable'])}"
        assert body["dateAvailable"] == expected["dateAvailable"], f"Expected dateAvailable {expected['dateAvailable']}, got {body['dateAvailable']}"
        
        # creationDate: string (date), nullable
        assert "creationDate" in body, "Response body missing 'creationDate' field"
        if expected.get("creationDate") is None:
            assert body.get("creationDate") is None, f"Expected creationDate to be None, got {body.get('creationDate')}"
        else:
            assert isinstance(body["creationDate"], str), f"Expected creationDate to be str, got {type(body['creationDate'])}"
            assert body["creationDate"] == expected["creationDate"], f"Expected creationDate {expected['creationDate']}, got {body['creationDate']}"
        
        # rating: number (double), not nullable
        assert "rating" in body, "Response body missing 'rating' field"
        assert isinstance(body["rating"], (int, float)), f"Expected rating to be number, got {type(body['rating'])}"
        assert body["rating"] == expected["rating"], f"Expected rating {expected['rating']}, got {body['rating']}"
        
        # ratingCount: integer (int32), not nullable
        assert "ratingCount" in body, "Response body missing 'ratingCount' field"
        assert isinstance(body["ratingCount"], int), f"Expected ratingCount to be int, got {type(body['ratingCount'])}"
        assert body["ratingCount"] == expected["ratingCount"], f"Expected ratingCount {expected['ratingCount']}, got {body['ratingCount']}"
        
        # rentalDuration: integer (int32), not nullable
        assert "rentalDuration" in body, "Response body missing 'rentalDuration' field"
        assert isinstance(body["rentalDuration"], int), f"Expected rentalDuration to be int, got {type(body['rentalDuration'])}"
        assert body["rentalDuration"] == expected["rentalDuration"], f"Expected rentalDuration {expected['rentalDuration']}, got {body['rentalDuration']}"
        
        # rentalPeriod: integer (int32), not nullable
        assert "rentalPeriod" in body, "Response body missing 'rentalPeriod' field"
        assert isinstance(body["rentalPeriod"], int), f"Expected rentalPeriod to be int, got {type(body['rentalPeriod'])}"
        assert body["rentalPeriod"] == expected["rentalPeriod"], f"Expected rentalPeriod {expected['rentalPeriod']}, got {body['rentalPeriod']}"
        
        # type: string, nullable
        assert "type" in body, "Response body missing 'type' field"
        if expected.get("type") is None:
            assert body.get("type") is None, f"Expected type to be None, got {body.get('type')}"
        else:
            assert isinstance(body["type"], str), f"Expected type to be str, got {type(body['type'])}"
            assert body["type"] == expected["type"], f"Expected type {expected['type']}, got {body['type']}"
        
        # descriptions: array of ProductDescription, not nullable
        assert "descriptions" in body, "Response body missing 'descriptions' field"
        assert isinstance(body["descriptions"], list), f"Expected descriptions to be list, got {type(body['descriptions'])}"
        assert len(body["descriptions"]) == len(expected["descriptions"]), f"Expected {len(expected['descriptions'])} descriptions, got {len(body['descriptions'])}"
        for i, desc in enumerate(body["descriptions"]):
            assert isinstance(desc, dict), f"Expected descriptions[{i}] to be dict, got {type(desc)}"
        assert body["descriptions"] == expected["descriptions"], f"Expected descriptions {expected['descriptions']}, got {body['descriptions']}"
        
        # categories: array of Category, not nullable
        assert "categories" in body, "Response body missing 'categories' field"
        assert isinstance(body["categories"], list), f"Expected categories to be list, got {type(body['categories'])}"
        assert len(body["categories"]) == len(expected["categories"]), f"Expected {len(expected['categories'])} categories, got {len(body['categories'])}"
        for i, cat in enumerate(body["categories"]):
            assert isinstance(cat, dict), f"Expected categories[{i}] to be dict, got {type(cat)}"
        assert body["categories"] == expected["categories"], f"Expected categories {expected['categories']}, got {body['categories']}"
        
        # productSpecifications: object, not nullable
        assert "productSpecifications" in body, "Response body missing 'productSpecifications' field"
        assert isinstance(body["productSpecifications"], dict), f"Expected productSpecifications to be dict, got {type(body['productSpecifications'])}"
        assert body["productSpecifications"] == expected["productSpecifications"], f"Expected productSpecifications {expected['productSpecifications']}, got {body['productSpecifications']}"
        
        # attributes: array of PersistableProductAttribute, nullable
        assert "attributes" in body, "Response body missing 'attributes' field"
        if expected.get("attributes") is None:
            assert body.get("attributes") is None, f"Expected attributes to be None, got {body.get('attributes')}"
        else:
            assert isinstance(body["attributes"], list), f"Expected attributes to be list, got {type(body['attributes'])}"
            assert len(body["attributes"]) == len(expected["attributes"]), f"Expected {len(expected['attributes'])} attributes, got {len(body['attributes'])}"
            for i, attr in enumerate(body["attributes"]):
                assert isinstance(attr, dict), f"Expected attributes[{i}] to be dict, got {type(attr)}"
            assert body["attributes"] == expected["attributes"], f"Expected attributes {expected['attributes']}, got {body['attributes']}"
        
        # images: array of PersistableImage, nullable
        assert "images" in body, "Response body missing 'images' field"
        if expected.get("images") is None:
            assert body.get("images") is None, f"Expected images to be None, got {body.get('images')}"
        else:
            assert isinstance(body["images"], list), f"Expected images to be list, got {type(body['images'])}"
            assert len(body["images"]) == len(expected["images"]), f"Expected {len(expected['images'])} images, got {len(body['images'])}"
            for i, img in enumerate(body["images"]):
                assert isinstance(img, dict), f"Expected images[{i}] to be dict, got {type(img)}"
            assert body["images"] == expected["images"], f"Expected images {expected['images']}, got {body['images']}"
        
        # productPrices: array of PersistableProductPrice, nullable
        assert "productPrices" in body, "Response body missing 'productPrices' field"
        if expected.get("productPrices") is None:
            assert body.get("productPrices") is None, f"Expected productPrices to be None, got {body.get('productPrices')}"
        else:
            assert isinstance(body["productPrices"], list), f"Expected productPrices to be list, got {type(body['productPrices'])}"
            assert len(body["productPrices"]) == len(expected["productPrices"]), f"Expected {len(expected['productPrices'])} productPrices, got {len(body['productPrices'])}"
            for i, price in enumerate(body["productPrices"]):
                assert isinstance(price, dict), f"Expected productPrices[{i}] to be dict, got {type(price)}"
            assert body["productPrices"] == expected["productPrices"], f"Expected productPrices {expected['productPrices']}, got {body['productPrices']}"
        
        # relatedProducts: array of RelatedProduct, nullable
        assert "relatedProducts" in body, "Response body missing 'relatedProducts' field"
        if expected.get("relatedProducts") is None:
            assert body.get("relatedProducts") is None, f"Expected relatedProducts to be None, got {body.get('relatedProducts')}"
        else:
            assert isinstance(body["relatedProducts"], list), f"Expected relatedProducts to be list, got {type(body['relatedProducts'])}"
            assert len(body["relatedProducts"]) == len(expected["relatedProducts"]), f"Expected {len(expected['relatedProducts'])} relatedProducts, got {len(body['relatedProducts'])}"
            for i, rel in enumerate(body["relatedProducts"]):
                assert isinstance(rel, dict), f"Expected relatedProducts[{i}] to be dict, got {type(rel)}"
            assert body["relatedProducts"] == expected["relatedProducts"], f"Expected relatedProducts {expected['relatedProducts']}, got {body['relatedProducts']}"
        
        # owner: object, not nullable
        assert "owner" in body, "Response body missing 'owner' field"
        assert isinstance(body["owner"], dict), f"Expected owner to be dict, got {type(body['owner'])}"
        assert body["owner"] == expected["owner"], f"Expected owner {expected['owner']}, got {body['owner']}"
        
        # Verify response body id matches product id
        assert body["id"] == int(product_id), f"Expected response id to match path parameter {product_id}, got {body['id']}"
        
        print(f"[PASS] {TEST_CASE_ID}: all assertions passed (status={response.status_code})")
    except AssertionError as e:
        print(f"[FAIL] {TEST_CASE_ID}: {e}")
        raise

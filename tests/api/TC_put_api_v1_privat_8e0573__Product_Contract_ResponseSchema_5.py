import os
import json
import pytest
import requests

from utilities.fs_data_utility import get_request_data, get_expected_response

BASE_URL = os.getenv("BASE_URL", "")
AUTH_HEADERS = json.loads(os.getenv("AUTH_HEADERS") or "{}")

TEST_CASE_ID = "TC_put_api_v1_privat_8e0573__Product_Contract_ResponseSchema_5"


def test_put_product_conforms_to_persistable_schema():
    """TC_put_api_v1_privat_8e0573__Product_Contract_ResponseSchema_5"""
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
        assert response.status_code == 200
        body = response.json()

        # Verify Content-Type header is application/json
        assert response.headers.get("Content-Type") == "application/json"

        # Verify every property listed in the schema is present with correct type and value
        # id: integer (int64), nullable: false
        assert "id" in body
        assert isinstance(body["id"], int)
        assert body["id"] == expected["id"]

        # sku: string, nullable: false
        assert "sku" in body
        assert isinstance(body["sku"], str)
        assert body["sku"] == expected["sku"]

        # refSku: string, nullable: false
        assert "refSku" in body
        assert isinstance(body["refSku"], str)
        assert body["refSku"] == expected["refSku"]

        # price: number, nullable: false
        assert "price" in body
        assert isinstance(body["price"], (int, float))
        assert body["price"] == expected["price"]

        # quantity: integer (int32), nullable: false
        assert "quantity" in body
        assert isinstance(body["quantity"], int)
        assert body["quantity"] == expected["quantity"]

        # available: boolean, nullable: false
        assert "available" in body
        assert isinstance(body["available"], bool)
        assert body["available"] == expected["available"]

        # visible: boolean, nullable: false
        assert "visible" in body
        assert isinstance(body["visible"], bool)
        assert body["visible"] == expected["visible"]

        # productShipeable: boolean, nullable: false
        assert "productShipeable" in body
        assert isinstance(body["productShipeable"], bool)
        assert body["productShipeable"] == expected["productShipeable"]

        # productVirtual: boolean, nullable: false
        assert "productVirtual" in body
        assert isinstance(body["productVirtual"], bool)
        assert body["productVirtual"] == expected["productVirtual"]

        # preOrder: boolean, nullable: false
        assert "preOrder" in body
        assert isinstance(body["preOrder"], bool)
        assert body["preOrder"] == expected["preOrder"]

        # productIsFree: boolean, nullable: false
        assert "productIsFree" in body
        assert isinstance(body["productIsFree"], bool)
        assert body["productIsFree"] == expected["productIsFree"]

        # quantityOrderMinimum: integer (int32), nullable: false
        assert "quantityOrderMinimum" in body
        assert isinstance(body["quantityOrderMinimum"], int)
        assert body["quantityOrderMinimum"] == expected["quantityOrderMinimum"]

        # quantityOrderMaximum: integer (int32), nullable: false
        assert "quantityOrderMaximum" in body
        assert isinstance(body["quantityOrderMaximum"], int)
        assert body["quantityOrderMaximum"] == expected["quantityOrderMaximum"]

        # sortOrder: integer (int32), nullable: false
        assert "sortOrder" in body
        assert isinstance(body["sortOrder"], int)
        assert body["sortOrder"] == expected["sortOrder"]

        # dateAvailable: string (date), nullable: false
        assert "dateAvailable" in body
        assert isinstance(body["dateAvailable"], str)
        assert body["dateAvailable"] == expected["dateAvailable"]

        # creationDate: string (date), nullable: true
        assert "creationDate" in body
        assert body["creationDate"] is None or isinstance(body["creationDate"], str)
        if expected.get("creationDate") is not None:
            assert body["creationDate"] == expected["creationDate"]
        else:
            assert body["creationDate"] is None

        # rating: number (double), nullable: false
        assert "rating" in body
        assert isinstance(body["rating"], (int, float))
        assert body["rating"] == expected["rating"]

        # ratingCount: integer (int32), nullable: false
        assert "ratingCount" in body
        assert isinstance(body["ratingCount"], int)
        assert body["ratingCount"] == expected["ratingCount"]

        # rentalDuration: integer (int32), nullable: false
        assert "rentalDuration" in body
        assert isinstance(body["rentalDuration"], int)
        assert body["rentalDuration"] == expected["rentalDuration"]

        # rentalPeriod: integer (int32), nullable: false
        assert "rentalPeriod" in body
        assert isinstance(body["rentalPeriod"], int)
        assert body["rentalPeriod"] == expected["rentalPeriod"]

        # type: string, nullable: true
        assert "type" in body
        assert body["type"] is None or isinstance(body["type"], str)
        if expected.get("type") is not None:
            assert body["type"] == expected["type"]
        else:
            assert body["type"] is None

        # descriptions: array of ProductDescription, nullable: false
        assert "descriptions" in body
        assert isinstance(body["descriptions"], list)
        assert len(body["descriptions"]) == len(expected["descriptions"])
        for i, desc in enumerate(body["descriptions"]):
            assert isinstance(desc, dict)
            assert desc == expected["descriptions"][i]

        # categories: array of Category, nullable: false
        assert "categories" in body
        assert isinstance(body["categories"], list)
        assert len(body["categories"]) == len(expected["categories"])
        for i, cat in enumerate(body["categories"]):
            assert isinstance(cat, dict)
            assert cat == expected["categories"][i]

        # productSpecifications: object, nullable: false
        assert "productSpecifications" in body
        assert isinstance(body["productSpecifications"], dict)
        assert body["productSpecifications"] == expected["productSpecifications"]

        # attributes: array of PersistableProductAttribute, nullable: true
        assert "attributes" in body
        assert body["attributes"] is None or isinstance(body["attributes"], list)
        if expected.get("attributes") is not None:
            assert len(body["attributes"]) == len(expected["attributes"])
            for i, attr in enumerate(body["attributes"]):
                assert isinstance(attr, dict)
                assert attr == expected["attributes"][i]
        else:
            assert body["attributes"] is None

        # images: array of PersistableImage, nullable: true
        assert "images" in body
        assert body["images"] is None or isinstance(body["images"], list)
        if expected.get("images") is not None:
            assert len(body["images"]) == len(expected["images"])
            for i, img in enumerate(body["images"]):
                assert isinstance(img, dict)
                assert img == expected["images"][i]
        else:
            assert body["images"] is None

        # productPrices: array of PersistableProductPrice, nullable: true
        assert "productPrices" in body
        assert body["productPrices"] is None or isinstance(body["productPrices"], list)
        if expected.get("productPrices") is not None:
            assert len(body["productPrices"]) == len(expected["productPrices"])
            for i, price in enumerate(body["productPrices"]):
                assert isinstance(price, dict)
                assert price == expected["productPrices"][i]
        else:
            assert body["productPrices"] is None

        # relatedProducts: array of RelatedProduct, nullable: true
        assert "relatedProducts" in body
        assert body["relatedProducts"] is None or isinstance(body["relatedProducts"], list)
        if expected.get("relatedProducts") is not None:
            assert len(body["relatedProducts"]) == len(expected["relatedProducts"])
            for i, rel_prod in enumerate(body["relatedProducts"]):
                assert isinstance(rel_prod, dict)
                assert rel_prod == expected["relatedProducts"][i]
        else:
            assert body["relatedProducts"] is None

        # owner: object, nullable: false
        assert "owner" in body
        assert isinstance(body["owner"], dict)
        assert body["owner"] == expected["owner"]

        # Verify no additional top-level fields appear beyond those defined in the schema
        expected_fields = {
            "id", "sku", "refSku", "price", "quantity", "available", "visible",
            "productShipeable", "productVirtual", "preOrder", "productIsFree",
            "quantityOrderMinimum", "quantityOrderMaximum", "sortOrder", "dateAvailable",
            "creationDate", "rating", "ratingCount", "rentalDuration", "rentalPeriod",
            "type", "descriptions", "categories", "productSpecifications", "attributes",
            "images", "productPrices", "relatedProducts", "owner"
        }
        assert set(body.keys()) == expected_fields

        print(f"[PASS] {TEST_CASE_ID}: all assertions passed (status={response.status_code})")
    except AssertionError as e:
        print(f"[FAIL] {TEST_CASE_ID}: {e}")
        raise

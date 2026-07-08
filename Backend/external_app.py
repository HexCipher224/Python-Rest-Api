import requests

BASE_URL = "https://world.openfoodfacts.org/api/v0/product"


def get_product_by_barcode(barcode):
    """
    Fetch product information from OpenFoodFacts using barcode.
    """

    url = f"{BASE_URL}/{barcode}.json"

    response = requests.get(url)

    if response.status_code != 200:
        return {"error": "Unable to connect to OpenFoodFacts"}

    data = response.json()

    if data.get("status") == 1:
        product = data["product"]

        return {
            "barcode": barcode,
            "name": product.get("product_name"),
            "brand": product.get("brands"),
            "category": product.get("categories"),
        }

    return {"error": "Product not found"}
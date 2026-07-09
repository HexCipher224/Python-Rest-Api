from flask import Flask, jsonify, request
from inventory import inventory
from flask_cors import CORS
import requests

app = Flask(__name__)

CORS(app)


# Home Route
@app.route("/")
def home():
    return jsonify({
        "message": "Inventory Management API",
        "status": "Running"
    })


# GET all items
@app.route("/items", methods=["GET"])
def get_items():
    return jsonify(inventory), 200


# GET one item
@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    for item in inventory:
        if item["id"] == item_id:
            return jsonify(item), 200

    return jsonify({"error": "Item not found"}), 404


# POST new item
@app.route("/items", methods=["POST"])
def add_item():
    data = request.get_json()

    new_item = {
        "id": len(inventory) + 1,
        "name": data["name"],
        "quantity": data["quantity"],
        "price": data["price"]
    }

    inventory.append(new_item)

    return jsonify(new_item), 201


# PATCH item
@app.route("/items/<int:item_id>", methods=["PATCH"])
def update_item(item_id):
    data = request.get_json()

    for item in inventory:
        if item["id"] == item_id:
            item["name"] = data.get("name", item["name"])
            item["quantity"] = data.get("quantity", item["quantity"])
            item["price"] = data.get("price", item["price"])

            return jsonify(item), 200

    return jsonify({"error": "Item not found"}), 404


# DELETE item
@app.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    global inventory

    for item in inventory:
        if item["id"] == item_id:
            inventory.remove(item)
            return jsonify({"message": "Item deleted"}), 200

    return jsonify({"error": "Item not found"}), 404


# Search OpenFoodFacts
@app.route("/product/<barcode>", methods=["GET"])
def get_product(barcode):
    url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"

    response = requests.get(url)

    if response.status_code != 200:
        return jsonify({"error": "Unable to contact OpenFoodFacts"}), 500

    data = response.json()

    if data.get("status") != 1:
        return jsonify({"error": "Product not found"}), 404

    product = data["product"]

    return jsonify({
        "barcode": barcode,
        "name": product.get("product_name"),
        "brand": product.get("brands"),
        "category": product.get("categories"),
        "quantity": product.get("quantity")
    })


if __name__ == "__main__":
    app.run(debug=True)
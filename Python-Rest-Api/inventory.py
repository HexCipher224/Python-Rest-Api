"""
inventory.py

Handles all inventory CRUD operations.
"""

inventory = []


def get_all_items():
    """Return all inventory items."""
    return inventory


def get_item(item_id):
    """Return a single item by its ID."""
    for item in inventory:
        if item["id"] == item_id:
            return item
    return None


def add_item(name, quantity, price):
    """Add a new inventory item."""

    new_item = {
        "id": len(inventory) + 1,
        "name": name,
        "quantity": quantity,
        "price": price
    }

    inventory.append(new_item)

    return new_item


def update_item(item_id, updates):
    """Update an existing inventory item."""

    item = get_item(item_id)

    if item is None:
        return None

    item["name"] = updates.get("name", item["name"])
    item["quantity"] = updates.get("quantity", item["quantity"])
    item["price"] = updates.get("price", item["price"])

    return item


def delete_item(item_id):
    """Delete an inventory item."""

    item = get_item(item_id)

    if item is None:
        return False

    inventory.remove(item)

    return True
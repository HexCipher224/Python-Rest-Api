import unittest
from app import app, inventory


class InventoryAPITestCase(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        app.testing = True

    def test_home_route(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_get_all_items(self):
        response = self.client.get("/items")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.get_json(), list)

    def test_get_single_item(self):
        if not inventory:
            inventory.append({
                "id": 1,
                "name": "Test Item",
                "quantity": 10,
                "price": 100
            })

        response = self.client.get("/items/1")
        self.assertEqual(response.status_code, 200)

    def test_add_item(self):
        new_item = {
            "name": "Keyboard",
            "quantity": 5,
            "price": 2500
        }

        response = self.client.post("/items", json=new_item)

        self.assertEqual(response.status_code, 201)

        data = response.get_json()

        self.assertEqual(data["name"], "Keyboard")
        self.assertEqual(data["quantity"], 5)
        self.assertEqual(data["price"], 2500)

    def test_update_item(self):
        if not inventory:
            inventory.append({
                "id": 1,
                "name": "Mouse",
                "quantity": 5,
                "price": 800
            })

        update_data = {
            "price": 1000
        }

        response = self.client.patch("/items/1", json=update_data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["price"], 1000)

    def test_delete_item(self):
        inventory.append({
            "id": 999,
            "name": "Delete Test",
            "quantity": 1,
            "price": 100
        })

        response = self.client.delete("/items/999")

        self.assertIn(response.status_code, [200, 204])

    def test_item_not_found(self):
        response = self.client.get("/items/5000")
        self.assertEqual(response.status_code, 404)

    def test_openfoodfacts_route(self):
        response = self.client.get("/product/737628064502")

        self.assertIn(response.status_code, [200, 404, 500])


if __name__ == "__main__":
    unittest.main()
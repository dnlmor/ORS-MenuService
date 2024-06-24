# tests/test_services.py
import unittest
from app.services import DishService
from app.models import Dish
from app.database import db_session

class TestDishService(unittest.TestCase):
    def setUp(self):
        self.dish_data = {
            "name": "Pizza Margherita",
            "description": "Classic pizza with tomatoes and mozzarella",
            "price": 8.99
        }

    def test_create_dish(self):
        dish = DishService.create_dish(**self.dish_data)
        self.assertIsNotNone(dish.id)

    def test_update_dish(self):
        dish = DishService.create_dish(**self.dish_data)
        updated_dish = DishService.update_dish(dish.id, name="Updated Pizza")
        self.assertEqual(updated_dish.name, "Updated Pizza")

    def test_delete_dish(self):
        dish = DishService.create_dish(**self.dish_data)
        success = DishService.delete_dish(dish.id)
        self.assertTrue(success)

    def tearDown(self):
        db_session.remove()

if __name__ == '__main__':
    unittest.main()

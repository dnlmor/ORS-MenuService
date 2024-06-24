# tests/test_models.py
import unittest
from app.models import Dish
from app.database import db_session

class TestDishModel(unittest.TestCase):
    def setUp(self):
        self.dish = Dish(name="Pizza Margherita", description="Classic pizza with tomatoes and mozzarella", price=8.99)

    def test_create_dish(self):
        db_session.add(self.dish)
        db_session.commit()
        self.assertIsNotNone(self.dish.id)

    def tearDown(self):
        db_session.remove()

if __name__ == '__main__':
    unittest.main()

# tests/test_schema.py
import unittest
from app import create_app
from app.models import db_session, Dish

class TestSchema(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def tearDown(self):
        db_session.remove()

    def test_create_dish(self):
        response = self.client.post('/graphql', json={'query': '''
            mutation {
                createDish(name: "Pizza Margherita", description: "Classic pizza with tomatoes and mozzarella", price: 8.99) {
                    dish {
                        id
                        name
                        description
                        price
                    }
                }
            }
        '''})
        self.assertEqual(response.status_code, 200)
        self.assertIn('data', response.json)

    def test_list_dishes(self):
        response = self.client.post('/graphql', json={'query': '''
            query {
                listDishes {
                    id
                    name
                    description
                    price
                }
            }
        '''})
        self.assertEqual(response.status_code, 200)
        self.assertIn('data', response.json)

if __name__ == '__main__':
    unittest.main()

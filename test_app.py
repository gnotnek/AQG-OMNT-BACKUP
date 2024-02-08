import unittest
from app import app

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_index_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'BE OF AQG', response.data)

    def test_generate_route(self):
        response = self.app.post('/generate', data={'materi': 'some material'})
        self.assertEqual(response.status_code, 200)  # Assuming the route returns a successful response

    def test_generator_route(self):
        response = self.app.post('/generator', data={'materi': 'some material'})
        self.assertEqual(response.status_code, 200)  # Assuming the route returns a successful response
        data = response.json
        # Add more assertions to validate the response data

if __name__ == '__main__':
    unittest.main()

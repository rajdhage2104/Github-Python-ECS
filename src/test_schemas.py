# tests/test_schemas.py
import unittest
from schemas import UsersSchema

class TestSchemas(unittest.TestCase):
    def test_users_schema(self):
        schema = UsersSchema()
        data = {
            'id': 1,
            'designation': 'Test Designation',
            'email': 'test@example.com',
            'first_name': 'Test',
            'is_admin': 'False',
            'last_name': 'User',
            'middle_name': 'abc',
            'oidc_id': 'test_oidc_id',
            'phone_number': '1234567890',
            'previous_exp': 'Test Experience'
        }
        result = schema.load(data)

        # Check if there are any validation errors
        self.assertFalse(result.get('errors'), f"Validation errors: {result.get('errors')}")

        # Check individual fields
        self.assertEqual(result['id'], 1)
        self.assertEqual(result['designation'], 'Test Designation')
        self.assertEqual(result['first_name'], 'Test')
        self.assertEqual(result['email'], 'test@example.com')
        self.assertEqual(result['is_admin'], 'False')
        self.assertEqual(result['last_name'], 'User')
        self.assertEqual(result['middle_name'], 'abc')
        self.assertEqual(result['oidc_id'], 'test_oidc_id')
        self.assertEqual(result['phone_number'], '1234567890')
        self.assertEqual(result['previous_exp'], 'Test Experience')

if __name__ == '__main__':
    unittest.main()

# tests/test_models.py
import unittest
from models import Users


class TestModels(unittest.TestCase):
    def test_user_model_creation(self):
        user = Users(
            designation='Test Designation',
            email='test@example.com',
            first_name='Test',
            is_admin='False',
            last_name='User',
            middle_name='abc',
            oidc_id='test_oidc_id',
            phone_number='1234567890',
            previous_exp='Test Experience'
        )
        self.assertEqual(user.designation, 'Test Designation')
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.first_name, 'Test')
        self.assertEqual(user.is_admin, 'False')
        self.assertEqual(user.last_name, 'User')
        self.assertEqual(user.middle_name, 'abc')
        self.assertEqual(user.oidc_id, 'test_oidc_id')
        self.assertEqual(user.phone_number, '1234567890')
        self.assertEqual(user.previous_exp, 'Test Experience')

        

    def test_user_model_init(self):
        user = Users(designation='Test Designation', email='test@example.com', first_name='Test', is_admin='False', last_name='User', middle_name='abc', oidc_id='test_oidc_id', phone_number='1234567890', previous_exp='Test Experience')
        self.assertEqual(user.designation, 'Test Designation')
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.first_name, 'Test')
        self.assertEqual(user.is_admin, 'False')
        self.assertEqual(user.last_name, 'User')
        self.assertEqual(user.middle_name, 'abc')
        self.assertEqual(user.oidc_id, 'test_oidc_id')
        self.assertEqual(user.phone_number, '1234567890')
        self.assertEqual(user.previous_exp, 'Test Experience')


if __name__ == '__main__':
    unittest.main()
        

from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        username = 'test@bikashsubedi.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email=username,
            password=password
        )

        self.assertEqual(user.email, username)
        self.assertTrue(user.check_password(password))

    def test_new_user_normalized(self):
        """Test the new user for normalized"""
        email = 'test@BIKASHSUBEDI.COM'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """test creating user with no email taht raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """Create=ing new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@bikashsubedi.com',
            'test123'
        )

        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

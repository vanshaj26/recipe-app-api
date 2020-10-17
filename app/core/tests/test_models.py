from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_succesful(self):
        email = 'vanshaj@gmail.com'
        password = 'qwerty'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        # lower email validate
        email = 'vanshaj@GMAIL.COM'
        user = get_user_model().objects.create_user(email, 'qwerty123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        # testing no email error
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_superuser(self):
        # Test a new superuser
        user = get_user_model().objects.create_superuser(
            'vanshaj.garg@gmail.com',
            'qwerty'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

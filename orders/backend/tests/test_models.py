from django.test import TestCase
from backend.models import User


class UserTest(TestCase):
    """
    Тестирование модели User
    """
    def setUp(self):
        User.objects.create(
            email='new@new.ru', company='Newusers', position='creator', first_name='John', last_name='Johnson'
        )

    def test__str__(self):
        user_new = User.objects.get(email='new@new.ru')
        self.assertEqual(
            user_new.__str__(), 'John Johnson')

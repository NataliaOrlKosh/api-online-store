from rest_framework import status
from django.test import TestCase
from rest_framework.test import APIClient, APITestCase
from django.urls import reverse
from ..models import Category, Product, Shop, Order, User

client = APIClient()


class CategoriesTest(TestCase):
    """
    Тестирование получения списка категорий
    """
    def setUp(self):

        Category.objects.create(name='first')
        Category.objects.create(name='second')
        Category.objects.create(name='third')

    def test_get_all_categories(self):

        self.assertEqual(Category.objects.count(), 3)


class ShopTest(APITestCase):

    def test_create_shop(self):
        """
        Тестирование создания магазина
        """
        response = client.post('http://127.0.0.1:8000/api/v1/shops/', json={'name': 'NewShop'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Shop.objects.count(), 1)

    def test_get_shop(self):
        """
        Тестирование олучения информации о  магазинах
        """
        response = client.get('http://127.0.0.1:8000/api/v1/shops')
        self.assertEqual(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)


class ProductTest(APITestCase):
    """
    Тестирование получения информации о продуктах
    """

    def setUp(self):
        Category.objects.create(name='New')
        Product.objects.create(name='A', category_id=1)
        Product.objects.create(name='B', category_id=1)
        Product.objects.create(name='C', category_id=1)
        Product.objects.create(name='D', category_id=1)

    def test_get(self):

        response = self.client.get(reverse('backend:products'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Product.objects.count(), 4)


class OrderTest(APITestCase):
    """
    Тестирование получения информации о заказах
    """

    def setUp(self):
        User.objects.create(
            email='new@new.ru', company='Newusers', position='creator', first_name='John', last_name='Johnson'
        )
        Order.objects.create(user_id=1, dt=2131, state='state')

    def test_get(self):

        response = self.client.get(reverse('backend:order'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

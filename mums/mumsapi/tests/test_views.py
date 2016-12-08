from rest_framework import status
from rest_framework.test import APITestCase


class ProductViewTests(APITestCase):
    def test_products_view_not_crash(self):
        result = self.client.get('/api/products/')

        self.assertEquals(result.status_code, status.HTTP_200_OK)


class CalculateCartPriceTests(APITestCase):
    fixtures = ['main.json']

    def test_products_view_not_crash(self):
        cart = {'cart': [
            {'id': 1, 'quantity': 3},
            {'id': 2, 'quantity': 3}
        ]}

        result = self.client.post('/api/cart/calculate/', cart, format='json')

        self.assertEquals(result.status_code, status.HTTP_200_OK)
        self.assertEquals(result.json()['price'], 13.32)

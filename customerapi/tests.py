from lib2to3.pgen2.token import tok_name
from urllib import request, response
from django.test import TestCase


class login(TestCase):
    def setUp(self):
        response = self.client.post('/api/login/', {
            "username": "sajjad5",
            "password": "hellosajjad"
        })
        self.assertEqual(response.status_code, 200)

# Create your tests here.


# class TestRestaurant(TestCase):
#     def test_restaurant_create(self):
#         response = self.client.get('api/restaurant')
#         self.assertEqual(response.status_code, 200)

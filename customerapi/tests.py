
from email import header
import json

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

from customerapi.models import Restaurant, Menu, Vote

class RestaurantTest(APITestCase):
    def test_listRestaurant(self):
        queryset = Restaurant.objects.all()
        print(queryset)
        # response = self.client.get('/api/restaurant' ,  headers={ 'Authorization': 'Token bb11edce6734b6139bdcf0e28f1c801b162d94e69eb4ef884eaafd9b900c785c' } )
        # self.assertEqual(response.status_code, status.HTTP_200_OK )
        #self.assertEqual(len(response.data), 0)
        # client = APIClient()
        # result = client.login(username='sajjad4', password='hellosajjad')
        # print(result)
        #token = Token.objects.get(user__username='sajjad4')
        #print(token)
        

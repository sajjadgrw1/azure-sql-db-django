# View which takes a request and returns a response

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from customerapi.models import Restaurant, Menu, Vote
from customerapi.serializers import RestaurantSerializer, MenuSerializer, VoteSerializer, UserSerializer, RegisterSerializer
from rest_framework.decorators import api_view, permission_classes

from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
import json
from django.db.models import Count
from django.contrib.auth import login

from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import DjangoModelPermissions

from rest_framework.views import APIView
from knox.auth import TokenAuthentication

from datetime import datetime
class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        response = super(LoginAPI, self).post(request, format=None)
        # response['username'] = user.username
        response.data['email'] = user.email
        response.data['username'] = user.username
        response.data['type'] = user.groups.all()[0].name
        # response.data['type'] = user.username
        return response

class LogoutAPI(KnoxLoginView):
    def get(self, request, format=None):
        # simply delete the token to force a login
        # request.user.auth_token.delete()
        return  JsonResponse("logout", safe=False)


# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class RestaurantAPI(generics.GenericAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,DjangoModelPermissions,)
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        restaurant = serializer.save()
        return Response(RestaurantSerializer(restaurant).data)
    def get(self, request, *args, **kwargs):
        return Response(self.get_serializer(Restaurant.objects.all(), many=True).data)

class MenuAPI(generics.GenericAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,DjangoModelPermissions,)
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        menu = serializer.save()
        return Response(MenuSerializer(menu).data)
    def get(self, request, *args, **kwargs):
        return Response(self.get_serializer(Menu.objects.all(), many=True).data)

class VoteAPI(generics.GenericAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,DjangoModelPermissions,)
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # delete user votes for today
        Vote.objects.filter(voteMenuDate=datetime.today().strftime('%Y-%m-%d') , userId=request.data['userId']).delete()
        
        vote = serializer.save()
        return Response(VoteSerializer(vote).data)
    def get(self, request, *args, **kwargs):
        return Response(self.get_serializer(Vote.objects.all(), many=True).data)

class ResultAPI(generics.GenericAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,DjangoModelPermissions,)
    queryset = Vote.objects.all()
    def get(self, request, *args, **kwargs):
        # todayRecords = Vote.objects.filter(voteMenuDate=datetime.today().strftime('%Y-%m-%d'))
        todayRecords = Vote.objects.filter(voteMenuDate=datetime.today().strftime('%Y-%m-%d'))
        ress = todayRecords.values('voteMenuId').annotate(vote_count=Count('voteMenuId') ).order_by('-vote_count')[:3]
        return Response(ress)
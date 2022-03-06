#Design your URL route here

from django.urls import path, re_path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings



#URLConf
urlpatterns=[

    re_path(r'^restaurant/?$', views.RestaurantAPI.as_view(), name='restaurant'),
    re_path(r'^restaurant/([0-9]+)/?$', views.RestaurantAPI.as_view(), name='restaurant'),

    re_path(r'^menu/?$', views.MenuAPI.as_view(), name='menu'),
    re_path(r'^menu/([0-9]+)/?$', views.MenuAPI.as_view(), name='menu'),

    re_path(r'^vote/?$', views.VoteAPI.as_view() , name='vote'),
    re_path(r'^vote/([0-9]+)/?$', views.VoteAPI.as_view() , name='vote'),

    re_path(r'^vote/result', views.ResultAPI.as_view() , name='result'),
    
]
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('test',views.Payel),
    path('search',views.search),
    path('search_action',views.search_action,name="search_action"),
    path('signup',views.signup),
    path('signup-action',views.signup_action,name="signup_action")
]

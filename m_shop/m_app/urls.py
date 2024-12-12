from django.urls import path,include
from m_app import views

urlpatterns=[
    path('',views.m_app_login),
    
]
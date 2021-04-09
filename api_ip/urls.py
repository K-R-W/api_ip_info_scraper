from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api_resp/', views.response, name='response'),
]
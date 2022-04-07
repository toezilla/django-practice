from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index),
    path('read/<id>/', views.read),
    path('create/', views.create),
    path('delete/', views.delete),
    path('update/<id>/', views.update)
]

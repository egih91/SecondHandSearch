from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
path('shop/', views.Add_store),
path('show/', views.Show_story),
path('chain/', views.CreateChain.as_view()),
]
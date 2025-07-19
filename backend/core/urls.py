from django.urls import path
from .views import prompt_handler

urlpatterns = [
    path('prompt/', prompt_handler),
]

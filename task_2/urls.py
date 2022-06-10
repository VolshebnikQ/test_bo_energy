from django.urls import path

from .views import *


urlpatterns = [
    path('', Task2.as_view(), name='task_2'),
]
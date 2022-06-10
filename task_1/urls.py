from django.urls import path

from .views import *


urlpatterns = [
    path('', Task1.as_view(), name='task_1'),
]
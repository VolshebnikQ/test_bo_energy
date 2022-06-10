from django.urls import path

from .views import *


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('requests/', Requests.as_view(), name = 'requests'),
    path('register/', RegisterUser.as_view(), name = 'register'),
    path('login/', LoginUser.as_view(), name = 'login'),
]
from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.views.generic.dates import DateMixin
from django.views.generic import View
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from main.forms import RegisterUserForm, LoginUserForm

from .models import Request
from .serializers import RequestSerializer

class Home(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'main/home.html')

class Requests(View):
    def get(self, request, *args, **kwargs):
        queryset_requests = Request.objects.all()
        user = User.objects.get(username=request.user)

        context =  {    'requests': RequestSerializer(queryset_requests, many=True).data,
                        'user': user
                    }

        return render(request, 'main/my_req.html', context)


class RegisterUser(DateMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'account/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))


class LoginUser(DateMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'account/login.html'

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

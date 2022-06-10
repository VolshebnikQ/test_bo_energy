from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseBadRequest, JsonResponse
from django.contrib.auth.models import User
import json

from .equation import solve_equation
from main.models import Request

class Task1(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'task_1/task_1.html')

    def post(self, request, *args, **kwargs):
        is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

        if is_ajax:
            data = json.load(request)
            equation = data.get('equation')
            x = solve_equation(equation)
            context = {
                'x': x,
            }

            if request.user:
                Request.objects.create(
                    user = User.objects.get(username=request.user),
                    request = equation,
                    response = x
                )

            return JsonResponse(context)
        else:
            return HttpResponseBadRequest('Неверный запрос')
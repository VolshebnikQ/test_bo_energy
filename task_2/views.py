from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseBadRequest, JsonResponse
from django.contrib.auth.models import User
import json

from .suggest import suggest_color
from main.models import Request


class Task2(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'task_2/task_2.html')

    def post(self, request, *args, **kwargs):
        is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

        if is_ajax:
            data = json.load(request)
            suggest = data.get('suggest')
            answer = suggest_color(suggest)
            context = {
                'answer': answer,
            }

            if request.user:
                Request.objects.create(
                    user = User.objects.get(username=request.user),
                    request = suggest,
                    response = answer
                )

            return JsonResponse(context)
        else:
            return HttpResponseBadRequest('Неверный запрос')
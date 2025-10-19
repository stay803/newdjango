from django.http import JsonResponse
from django.shortcuts import render


def home(request):
    return render(request, "core/home.html", {"title": "首页"})


def health(request):
    return JsonResponse({"status": "ok"})

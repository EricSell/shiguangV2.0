from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return JsonResponse({"code": 1, "msg": '测试成功'})
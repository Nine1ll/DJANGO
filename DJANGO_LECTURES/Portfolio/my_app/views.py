from django.shortcuts import render
from django.http.response import HttpResponse

# 단순 함수
def index(request):
    return HttpResponse("HELLO THIS IS A VIEW INSIDE MY APP")
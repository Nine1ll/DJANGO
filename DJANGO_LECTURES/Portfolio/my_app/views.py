from django.shortcuts import render
from django.http.response import HttpResponse

# 단순 함수
article = {
    'sports':'Sports Page',
    'finance': 'Finance Page',
    'politics': 'Politics Page'
}

def news_view(request, topic):
    return HttpResponse(article[topic])

def index(request):
    return HttpResponse("HELLO THIS IS A VIEW INSIDE MY APP")

# def sport_view(request):
#     return HttpResponse(article['sports'])

# def finance_view(reqest):
#     return HttpResponse(article['finance'])

def add_view(request, num1, num2):
    add_result = num1 + num2
    result = f"{num1}+{num2} = {add_result}"
    return HttpResponse(str(result)) 
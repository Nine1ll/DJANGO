from pydoc_data.topics import topics
from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseNotFound, Http404

# 단순 함수
article = {
    'sports':'Sports Page',
    'finance': 'Finance Page',
    'politics': 'Politics Page'
}

def news_view(request, topic):
    try:
        result = article[topics]
        return HttpResponse(article[topic])
    except :
        # result = "No page for that topic"
        # return HttpResponseNotFound(result)
        raise Http404('404 GENERIC ERROR') # 404.html 과 연결 가능
    ## You’re seeing this error because you have DEBUG = True in your Django settings file. Change that to False, and Django will display a standard 404 page.
    ## 웹사이트 배포시 DEBUG == false
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
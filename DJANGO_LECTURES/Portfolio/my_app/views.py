from pydoc_data.topics import topics
from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.urls import reverse
# 단순 함수
article = {
    'sports':'Sports Page',
    'finance': 'Finance Page',
    'politics': 'Politics Page'
}

def index(request):
    return HttpResponse("HELLO THIS IS A VIEW INSIDE MY APP")

def news_view(request, topic):
    try:
        result = article[topic]
        return HttpResponse(result)
    except :
        raise Http404('404 GENERIC ERROR') # 404.html 과 연결 가능

# def add_view(request, num1, num2):
#     add_result = num1 + num2
#     result = f"{num1}+{num2} = {add_result}"
#     return HttpResponse(str(result)) 

# # domain.com/my_app/0 ----> finance or sports .... 
def num_page_view(request, num_page):
    topics_list = list(article.keys())
    topic = topics_list[num_page]
    HttpResponse(f"topic:{topic}")
    try:
        urls_please = reverse('topic-page',args=[topic])
        return HttpResponseRedirect(urls_please)
    except:
        raise HttpResponseNotFound("아 제발 실행좀 되게 해주세요.")

def simple_view(request):
    return render(request, 'my_app/example.html') # .html 파일이 있는데 
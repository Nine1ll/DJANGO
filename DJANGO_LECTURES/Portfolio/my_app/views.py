from pydoc_data.topics import topics
from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.urls import reverse
# 단순 함수
# article = {
#     'sports':'Sports Page',
#     'finance': 'Finance Page',
#     'politics': 'Politics Page'
# }

# def index(request):
#     return HttpResponse("HELLO THIS IS A VIEW INSIDE MY APP")

# def news_view(request, topic):
#     try:
#         result = article[topic  ]
#         return HttpResponse(result)
#     except :
#         raise Http404('404 GENERIC ERROR') # 404.html 과 연결 가능
    
# # def sport_view(request):
# #     return HttpResponse(article['sports'])

# # def finance_view(reqest):
# #     return HttpResponse(article['finance'])

# def add_view(request, num1, num2):
#     add_result = num1 + num2
#     result = f"{num1}+{num2} = {add_result}"
#     return HttpResponse(str(result)) 

# # domain.com/my_app/0 ----> finance or sports .... 
# def num_page_view(request,num_page):
    
#     topics_list = list(article.keys())
#     topic = topics_list[num_page]
        
#     return HttpResponseRedirect(reverse('topic-page',args=[topic]))

def simple_view(request):
    return render(request, 'my_app/example.html') # .html 파일이 있는데 
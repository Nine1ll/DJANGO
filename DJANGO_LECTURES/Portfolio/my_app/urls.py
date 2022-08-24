from django.urls import path
from . import views

# 기본적으로 path 속 ''에는 my_app/ 이 포함된 상황임.
urlpatterns = [
    path('',views.index,name='index')
]

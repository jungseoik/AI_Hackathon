from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('Web/', views.web_index),
    path('imdex/', views.imdex),
    path('input_text/', views.input_text, name='input_text'),
    path('home', views.home, name='home'),  # 루트 URL을 home 뷰와 연결
]
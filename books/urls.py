from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test_query_0, name='test_query_0'),
    path('test1/', views.test_query_1, name='test_query_1'),
    path('test2/', views.test_query_2, name='test_query_2'),
] 
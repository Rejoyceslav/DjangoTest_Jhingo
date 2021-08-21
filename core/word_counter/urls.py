from . import views
from django.urls import path


urlpatterns = [
    path('wordcounter/', views.word_counter, name='word_counter'),
    path('wordcounter/counter_result', views.counter_result, name='counter_result'),
    path('wordcounter/counter_result/counter_result_deeper', views.counter_result_deeper, name='counter_result_deeper'),
]

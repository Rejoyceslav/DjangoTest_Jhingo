from . import views
from django.urls import path


urlpatterns = [
    path('test/', views.test_model_form_view, name='test'),
    path('test_api/', views.test_api_view, name='test_api'),
]

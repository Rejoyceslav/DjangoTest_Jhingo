from . import views
from django.urls import path


urlpatterns = [
    path('test/', views.test_model_form_view, name='test'),
]

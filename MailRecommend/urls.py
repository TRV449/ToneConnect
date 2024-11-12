# urls.py
from django.urls import path
from .views import GenerateKeywordsAPIView, GenerateMailAPIView

urlpatterns = [
    path('generate_keywords/', GenerateKeywordsAPIView.as_view(), name='generate_keywords'),
    path('write_mail/', GenerateMailAPIView.as_view(), name='write_mail'),
]

# urls.py
from django.urls import path
from .views import ProfessorResponseView

urlpatterns = [
    path("professor/", ProfessorResponseView.as_view(), name="professor_response"),
    ]
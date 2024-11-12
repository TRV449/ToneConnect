# urls.py
from django.urls import path
from .views import ProfessorResponseView, StudentResponseView

urlpatterns = [
    path("professor/", ProfessorResponseView.as_view(), name="professor_response"),
    path("student/", StudentResponseView.as_view(), name="student_response"),
]
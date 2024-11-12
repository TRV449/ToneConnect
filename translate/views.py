# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .gpt_translate import generate_professor_response, generate_student_response


class ProfessorResponseView(APIView):
    def post(self, request):
        message = request.data.get("message")
        if not message:
            return Response({"error": "Message is required"}, status=status.HTTP_400_BAD_REQUEST)

        # 교수 역할의 응답 생성
        response_content = generate_professor_response(message)
        return Response({"response": response_content}, status=status.HTTP_200_OK)

class StudentResponseView(APIView):
    def post(self, request):
        message = request.data.get("message")
        if not message:
            return Response({"error": "Message is required"}, status=status.HTTP_400_BAD_REQUEST)

        # 학생 역할의 응답 생성
        response_content = generate_student_response(message)
        return Response({"response": response_content}, status=status.HTTP_200_OK)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Home, CV, About, Skill, Project, Experience
from .serializers import (
    HomeSerializer,
    CVSerializer,
    AboutSerializer,
    SkillSerializer,
    ProjectSerializer,
    ExperienceSerializer,
    ContactSerializer,
)


class HomeAPIView(APIView):
    def get(self, request):
        home = Home.objects.first()
        serializer = HomeSerializer(home, context={"request": request})
        return Response(serializer.data)


class CVAPIView(APIView):
    def get(self, request):
        cv = get_object_or_404(CV, is_active=True)
        response = FileResponse(cv.document.open('rb'), as_attachment=True, filename=cv.document.name)
        return response


class AboutAPIView(APIView):
    def get(self, request):
        about = About.objects.first()
        serializer = AboutSerializer(about)
        return Response(serializer.data)


class SkillAPIView(APIView):
    def get(self, request):
        skills = Skill.objects.all()
        serializer = SkillSerializer(skills, many=True)
        return Response(serializer.data)


class ProjectAPIView(APIView):
    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True, context={"request": request})
        return Response(serializer.data)


class ExperienceAPIView(APIView):
    def get(self, request):
        experiences = Experience.objects.all()
        serializer = ExperienceSerializer(experiences, many=True, context={"request": request})
        return Response(serializer.data)


class ContactView(APIView):
    serializer_class = ContactSerializer

    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            # Сохраняем в базу
            contact = serializer.save()

            # Отправляем письмо
            subject = "Новое сообщение с портфолио"
            message = f"Сообщение от: {contact.sender_email}\n\n{contact.sender_message}"

            send_mail(
                subject,
                message,
                contact.sender_email,              # от кого (можно заменить на DEFAULT_FROM_EMAIL)
                ['matackubovaslan@gmail.com'],        # кому (твоя почта)
                fail_silently=False,
            )

            return Response({"message": "Письмо отправлено"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
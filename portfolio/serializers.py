from rest_framework import serializers
from .models import Contact
from rest_framework import serializers
from .models import Home, CV, About, Skill, Project, Experience


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = ["photo", "name", "who_am_i", "focus"]


class CVSerializer(serializers.ModelSerializer):
    class Meta:
        model = CV
        fields = ["document", "is_active"]


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ["info"]


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ["name"]


class ProjectSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ["name", "content", "image", "skills", "link"]


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ["time", "icon", "main_info", "next_info"]

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['sender_email', 'sender_message']
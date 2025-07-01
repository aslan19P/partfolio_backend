from django.urls import path
from .views import (
    HomeAPIView,
    CVAPIView,
    AboutAPIView,
    SkillAPIView,
    ProjectAPIView,
    ExperienceAPIView,
    ContactView,
)

urlpatterns = [
    path('home/', HomeAPIView.as_view(), name='home'),
    path('cv/', CVAPIView.as_view(), name='cv'),
    path('about/', AboutAPIView.as_view(), name='about'),
    path('skills/', SkillAPIView.as_view(), name='skills'),
    path('projects/', ProjectAPIView.as_view(), name='projects'),
    path('experience/', ExperienceAPIView.as_view(), name='experience'),
    path('contact/', ContactView.as_view(), name='contact'),
]
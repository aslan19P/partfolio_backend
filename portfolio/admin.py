from django.contrib import admin
from .models import (
    CV, Home, About, Skill,
    Project, Experience, Contact
)


class HomeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'who_am_i', 'focus')
    search_fields = ('name', 'who_am_i')

class CVAdmin(admin.ModelAdmin):
    list_display = ('id', 'document', 'is_active')
    search_fields = ('document',)
    list_editable = ['is_active']

class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'info',)

class SkilsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name',)

class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'content', 'display_skills', 'link')
    search_fields = ('name', 'content')
    filter_horizontal = ('skills',)

    def display_skills(self, obj):
        return ", ".join([skill.name for skill in obj.skills.all()])
    display_skills.short_description = "Навыки"

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('id', 'time', 'main_info', 'next_info')
    search_fields = ('main_info', 'next_info')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender_email', 'sender_message')
    search_fields = ('sender_email',)


admin.site.register(Home, HomeAdmin)
admin.site.register(CV, CVAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Skill, SkilsAdmin)
admin.site.register(Project, ProjectsAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Contact, ContactAdmin)
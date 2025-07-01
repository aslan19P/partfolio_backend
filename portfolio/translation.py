from modeltranslation.translator import register, TranslationOptions
from .models import CV, Home, About, Project, Experience, Skill

@register(Home)
class HomeTranslationOptions(TranslationOptions):
    fields = ('name', 'who_am_i', 'focus')


@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('info',)


@register(Project)
class ProjectsTranslationOptions(TranslationOptions):
    fields = ('name', 'content')


@register(Experience)
class ExperienceTranslationOptions(TranslationOptions):
    fields = ('time', 'main_info', 'next_info')

@register(CV)
class CVTranslationOptions(TranslationOptions):
    fields = ('document', )
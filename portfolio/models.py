from django.db import models
from tinymce.models import HTMLField


class Home(models.Model):
    photo = models.ImageField(upload_to='photoes/', verbose_name="Фотографии")
    name = models.CharField(max_length=255, verbose_name="Имя")
    who_am_i = models.CharField(max_length=255, verbose_name="Кто я")
    focus = models.CharField(max_length=255, verbose_name="Фокус")

    class Meta:
        verbose_name = "Главная"
        verbose_name_plural = "Главная"

    def __str__(self):
        return self.name


class CV(models.Model):
    document = models.FileField(upload_to="cv/", verbose_name="Резюме")
    is_active = models.BooleanField(default=True, verbose_name="Действующий")

    class Meta:
        verbose_name = "Резюме"
        verbose_name_plural = "Резюме"

    def __str__(self):
        return self.document.name


class About(models.Model):
    info = HTMLField(verbose_name="Информация")

    class Meta:
        verbose_name = "Обо мне"
        verbose_name_plural = "Обо мне"

    def __str__(self):
        return "Информация обо мне"


class Skill(models.Model):
    name = models.CharField(max_length=255, verbose_name="Навык")

    class Meta:
        verbose_name = "Навык"
        verbose_name_plural = "Навыки"

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    content = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='project_images/', verbose_name="Изображение")
    skills = models.ManyToManyField(Skill, related_name='projects', verbose_name="Навыки")
    link = models.URLField(verbose_name="Ссылка на проект")

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

    def __str__(self):
        return self.name


class Experience(models.Model):
    time = models.CharField(max_length=225, verbose_name="Период")
    icon = models.ImageField(upload_to='icons/', verbose_name="Иконка")
    main_info = models.CharField(max_length=255, verbose_name="Основная информация")
    next_info = models.CharField(max_length=255, verbose_name="Дополнительная информация")

    class Meta:
        verbose_name = "Опыт"
        verbose_name_plural = "Опыт"

    def __str__(self):
        return f"{self.main_info} ({self.time})"


class Contact(models.Model):
    sender_email = models.EmailField(verbose_name='Email отправителя')
    sender_message = models.TextField(verbose_name="Сообщение")

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"

    def __str__(self):
        return f"Сообщение от {self.sender_email}"
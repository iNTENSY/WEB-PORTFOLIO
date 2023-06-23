from django.db import models


class Skill(models.Model):
    """Модель умений персонажа."""
    name = models.CharField(
        verbose_name='Заголовок',
        max_length=50
    )
    created = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )
    on_main = models.BooleanField(
        verbose_name='На главную?',
        default=False
    )

    class Meta:
        verbose_name = 'Умение'
        verbose_name_plural = 'Умения'

    def __str__(self):
        return self.name


class Project(models.Model):
    """Модель с определением всех проектов"""
    title = models.CharField(
        verbose_name='Название проекта',
        max_length=120
    )
    project_url = models.URLField(
        unique=True
    )
    on_main = models.BooleanField(
        verbose_name='На главную?',
        default=False
    )

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return self.title


class Goal(models.Model):
    """Модель с основными целями."""
    text = models.CharField(
        max_length=100,
        unique=True
    )
    on_main = models.BooleanField(
        verbose_name='На главную?',
        default=False
    )

    class Meta:
        verbose_name = 'Цель'
        verbose_name_plural = 'Цели'

    def __str__(self):
        return self.text

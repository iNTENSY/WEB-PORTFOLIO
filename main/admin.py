from django.contrib import admin

from .models import Skill, Project, Goal


@admin.register(Skill)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'on_main')


@admin.register(Project)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('title', 'on_main')


@admin.register(Goal)
class GoalsAdmin(admin.ModelAdmin):
    list_display = ('text', 'on_main')

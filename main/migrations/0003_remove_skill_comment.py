# Generated by Django 4.2.2 on 2023-06-23 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_goal_project_skill_delete_blogpost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='comment',
        ),
    ]

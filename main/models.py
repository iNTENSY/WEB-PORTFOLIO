from django.db import models


class BlogPost(models.Model):
    """Модель блог-постов для сайта."""
    title = models.CharField(
        verbose_name='Заголовок',
        max_length=200
    )
    comment = models.TextField(
        verbose_name='Комментарий'
    )
    project_url = models.URLField(
        verbose_name='Ссылка на проект'
    )
    image = models.ImageField(
        verbose_name='Обложка',
        blank=True,
        null=True,
        upload_to='media/'
    )
    created = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Блог-пост'
        verbose_name_plural = 'Блог-посты'

    def __str__(self):
        return self.title

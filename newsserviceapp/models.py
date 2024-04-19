from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class News(models.Model):
    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=255, verbose_name='Заголовок статьи')
    text = models.TextField(verbose_name='Текст статьи')
    author = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Автор статьи')


class Comment(models.Model):
    date = models.DateField(auto_now_add=True)
    text = models.TextField(verbose_name='Текст комментария')
    news = models.ForeignKey(News, on_delete=models.CASCADE, verbose_name='Новость')
    author = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Автор комментария')


class Like(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор лайка')
    news = models.ForeignKey(News, on_delete=models.CASCADE, verbose_name='Новость')
    # isLiked = models.BooleanField(default=False, verbose_name='Лайк')

    class Meta:
        unique_together = ('author', 'news')

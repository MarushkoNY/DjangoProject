from django.db import models

# Create your models here.

class Article(models.Model):
    class Meta():
        db_table = 'Article'
    article_title = models.CharField(max_length=100)
    article_text = models.TextField()
    article_datetime = models.DateTimeField()
    article_likes = models.IntegerField(default=0)

class Comments(models.Model):
    class Meta():
        db_table = 'Comments'
    comment_text = models.TextField(verbose_name='Comment text:')
    comment_article = models.ForeignKey(Article)
    comment_author = models.CharField(max_length=100, default='Nemo')








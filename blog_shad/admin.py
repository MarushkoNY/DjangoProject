from django.contrib import admin
from .models import Article, Comments

# Register your models here.
class ArticleInline(admin.StackedInline):
    model = Comments
    extra = 2

class ArticleAdmin(admin.ModelAdmin):
    fields = ['article_title', 'article_text', 'article_datetime']
    inlines = [ArticleInline]
    list_filter = ['article_datetime']

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comments)

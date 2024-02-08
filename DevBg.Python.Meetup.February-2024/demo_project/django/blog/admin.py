from django.contrib import admin
from .models import Comment, Article, Reaction

# Register your models here.
admin.site.register(Comment)
admin.site.register(Article)
admin.site.register(Reaction)

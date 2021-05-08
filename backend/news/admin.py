from django.contrib import admin
from .models import *

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
	list_display = (
		'headline',
		'author',
		'pub_date',
		'publish'
	)

admin.site.register(Article, ArticleAdmin)
admin.site.register(Author)
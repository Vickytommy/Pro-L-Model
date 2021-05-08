from django.contrib import admin
from .models import FashionModel, FashionModelImage

# Register your models here.
class FashionModelImageAdmin(admin.StackedInline):
	model = FashionModelImage

@admin.register(FashionModel)
class FashionModelAdmin(admin.ModelAdmin):
	list_display = (
		'first_name',
		'last_name',
		'stage_name',
		'age',
		'sex',
		'height',
		'bio',
		'photo'
	)

	inlines = [FashionModelImageAdmin]

	class Meta:
		model = FashionModel

@admin.register(FashionModelImage)
class FashionModelImageAdmin(admin.ModelAdmin):
	pass
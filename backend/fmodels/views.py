from django.shortcuts import render
from rest_framework import viewsets, filters
from .serializers import FashionModelSerializer
from .models import FashionModel, FashionModelImage

# Create your views here.
class FashionModelView(viewsets.ModelViewSet):
	search_fields = [
		'first_name',
		'last_name',
		'stage_name',
		'=sex'
	]
	filter_backends = (filters.SearchFilter,)
	serializer_class = FashionModelSerializer
	queryset = FashionModel.objects.all()

class FashionModelImageView(viewsets.ModelViewSet):
	serializer_class = FashionModelSerializer
	queryset = FashionModelImage.objects.all()
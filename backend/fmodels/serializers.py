from rest_framework import serializers
from .models import FashionModel, FashionModelImage

class FashionModelImageSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = FashionModelImage
		fields = ['picture']

class FashionModelSerializer(serializers.ModelSerializer):
	images = FashionModelImageSerializer(
		many=True
	)

	class Meta:
		model = FashionModel
		fields = [
			'id',
			'first_name',
			'last_name',
			'stage_name',
			'age',
			'sex',
			'height',
			'chest',
			'shoulder',
			'waist',
			'butt',
			'bio',
			'photo',
			'images'
		]

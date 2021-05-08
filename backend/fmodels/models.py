from django.db import models

# Create your models here.
class FashionModel(models.Model):
	first_name = models.CharField(max_length = 50)
	last_name = models.CharField(max_length = 50)
	stage_name = models.CharField(max_length = 30)
	age = models.IntegerField()

	SEX = [
		('MALE', 'Male'),
		('FEMALE', 'Female'),
	]
	sex = models.CharField(max_length=6, choices=SEX)
	height = models.IntegerField()

	# Male selections
	chest = models.IntegerField()
	shoulder = models.IntegerField()

	#Female selections
	waist = models.IntegerField()
	butt = models.IntegerField()

	bio = models.TextField()
	
	# FileField args - upload_to='uploads/'
	photo = models.FileField(upload_to='model_images/', null=True, verbose_name="")


	class Meta:
		db_table = "ProL Models"


class FashionModelImage(models.Model):
	album = models.ForeignKey(FashionModel, related_name='images', on_delete=models.CASCADE)
	picture = models.FileField(upload_to='model_images/', verbose_name="")

	class Meta:
		unique_together = ['album', 'picture']
		ordering = ['picture']

	def __str__(self):
		return '%s' % (self.picture)
from django.db import models

# Create your models here.
class Author(models.Model):
	first_name = models.CharField(max_length = 30)
	last_name = models.CharField(max_length = 30)

	def __str__(self):
		return f"{self.last_name}, {self.first_name}"


class Article(models.Model):
	headline = models.CharField(max_length = 120)
	description = models.CharField(max_length = 300)
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	content = models.TextField(max_length = 10000)
	pub_date = models.DateField()
	publish = models.BooleanField(default = True)

	def __str__(self):
		return self.headline

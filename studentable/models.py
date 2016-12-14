from django.db import models
from django.utils import timezone

# Create your models here.

class Course(models.Model):
	code = models.CharField(max_length=6)
	mon = models.CharField(max_length=12)
	tue = models.CharField(max_length=12)
	wed = models.CharField(max_length=12)
	thu = models.CharField(max_length=12)
	fri = models.CharField(max_length=12)

	def __str__(self):
		return self.code
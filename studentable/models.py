from django.db import models
from django.utils import timezone

# Create your models here.

class Course(models.Model):
	code = models.CharField(max_length=6)
	mon = models.CharField(max_length=12, default=' ')
	tue = models.CharField(max_length=12, default=' ')
	wed = models.CharField(max_length=12, default=' ')
	thu = models.CharField(max_length=12, default=' ')
	fri = models.CharField(max_length=12, default=' ')

	def __str__(self):
		return self.code.upper()
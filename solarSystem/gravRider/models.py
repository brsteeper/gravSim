from django.db import models

class Body(models.Model):
	name = models.CharField(max_length = 50)
	mass = models.FloatField()

	def __str__(self):
		return self.name
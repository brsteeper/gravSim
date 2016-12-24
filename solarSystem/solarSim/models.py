#solarSim

from django.db import models

class Planet(models.Model):
	name = models.CharField(max_length = 50)
	mass = models.FloatField()
	
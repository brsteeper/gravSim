#solarSim

from django.db import models

class Planet(models.Model):
	name = models.CharField(max_length = 50)
	mass = models.FloatField()
	x = models.FloatField(default = 2E+10)
	y = models.FloatField(default = 0)
	z = models.FloatField(default = 0)
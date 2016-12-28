#solarSim

from django import forms

class CreatePlanetForm(forms.Form):
	planet_name = forms.CharField(label='Planet Name', max_length = 50)
	planet_mass = forms.FloatField(label='Planet Mass')
	planet_x = forms.FloatField(label='Planet x Coordinate (km)', initial=3E+10)
	planet_y = forms.FloatField(label='Planet y Coordinate (km)', initial=0)
	planet_z = forms.FloatField(label='Planet z Coordinate (km)', initial=0)
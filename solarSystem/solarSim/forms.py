#solarSim

from django import forms

class planetStatsForm(forms.Form):
	planet_name = forms.CharField(label='Planet Name', max_length = 50)
	planet_mass = forms.FloatField(label='Planet Mass')
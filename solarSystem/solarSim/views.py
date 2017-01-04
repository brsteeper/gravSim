#solarSim

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import CreatePlanetForm
from .models import Planet
from django.forms.models import model_to_dict
import json

def index (request):
	if request.method == 'POST':
		form = CreatePlanetForm(request.POST)
		if form.is_valid():
			planet = Planet()
			planet.name = form.cleaned_data["planet_name"]
			planet.mass = form.cleaned_data["planet_mass"]
			planet.x = form.cleaned_data["planet_x"]
			planet.y = form.cleaned_data["planet_y"]
			planet.z = form.cleaned_data["planet_z"]
			planet.save()
			#return render(request, 'solarSim/display.html', {'planetID': planet.id}) #I want this to call display through its def in this file not through the .html. I think?
			return redirect('display', planet.id)
	else:
		form = CreatePlanetForm
		return render(request, 'solarSim/index.html', {'form': form, 'action_path' : request.path})

def display (request, planetID):
	planet = Planet.objects.get(pk=planetID)
	dict_planet = model_to_dict(planet)
	json_planet = json.dumps(dict_planet)

	content = {'planet' : json_planet}
	#content = {'planet': planet}
	#import pdb; pdb.set_trace()

	return render(request, 'solarSim/display.html', content)

#solarSim

from django.http import HttpResponse
from django.shortcuts import render
from .forms import CreatePlanetForm
from .models import Planet

def index (request):
	if request.method == 'POST':
		form = CreatePlanetForm(request.POST)
		if form.is_valid():
			planet = Planet()
			planet.name = form.cleaned_data["planet_name"]
			planet.mass = form.cleaned_data["planet_mass"]
			planet.save()
			return render(request, 'solarSim/display.html', {'planetID': planet.id}) #I want this to call display through its def in this file not through the .html. I think?
	else:
		form = CreatePlanetForm
		return render(request, 'solarSim/index.html', {'form': form, 'action_path' : request.path})

def display (request, planetID):
	planet = Planet.objects.get(pk=plantID)
	return render(request, 'solarSim/display.html', {'planet': planet})

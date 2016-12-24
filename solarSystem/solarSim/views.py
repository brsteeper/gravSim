#solarSim

from django.http import HttpResponse
from django.shortcuts import render
from .forms import CreatePlanetForm

def index (request):
#	content = {'planet_name':'Jupiter',
#				'mass':778000000}
	form = CreatePlanetForm
	return render(request, 'solarSim/index.html', {'form': form})

def display (request):
	return render(request, 'solarSim/display.html')

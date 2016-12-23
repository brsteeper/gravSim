#solarSim

from django.http import HttpResponse
from django.shortcuts import render

def index (request):
	return render(request, 'solarSim/index.html')

def plot (request):
	return HttpResponse('Tang!')

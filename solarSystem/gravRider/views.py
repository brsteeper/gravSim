#gravSim

from django.shortcuts import render
from django.http import HttpResponse

def visualization(request):
	content = {'stuff':1234}
	return render(request, 'gravRider/visualization.html', content)

def form(request):
	return render(request, 'gravRider/form.html')

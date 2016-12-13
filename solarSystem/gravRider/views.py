from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	content = {'stuff':1234}
	return render(request, 'gravRider/visualization.html', content)



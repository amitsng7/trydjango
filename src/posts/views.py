from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def post_create(request):
	context={
		"title":"create"
	}
	return render(request, "index.html", context)

def post_index(request):
	context={
		"title":"index"
	}
	return render(request, "index.html", context)

def post_delete(request):
	context={
		"title":"delete"
	}
	return render(request, "index.html", context)

def post_update(request):
	context={
		"title":"update"
	}
	return render(request, "index.html", context)
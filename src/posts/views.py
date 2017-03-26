from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from posts.models import Post

# Create your views here.
def post_create(request):
	context={
		"title":"create"
	}
	return render(request, "index.html", context)

def post_index(request,id=None):
	if(id==None):
		instance=Post.objects.all()
		context={
			"instance":instance,
			"title":"Index All"
		}
		return render(request, "indexAll.html", context)
	else:
		instance=get_object_or_404(Post, id=id)
		context={
			"instance":instance,
			"title":instance.title
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
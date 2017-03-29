from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from posts.models import Post
from .form import PostForm

# Create your views here.
def post_create(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		messages.success(request, "Successfully Created")
	else:
		messages.error(request, "Not Successfully Created")
	context={
		"form":form
	}
	return render(request, "post_create.html", context)

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

def post_update(request, id=None):
	instance=get_object_or_404(Post, id=id)
	form=PostForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()		
		messages.success(request, "Successfully Saved")
	else:
		messages.error(request, "Not Successfully saved")
	context={
		"instance":instance,
		"title":instance.title,
		"form":form
	}
	return render(request, "post_create.html", context)

def post_delete(request, id):
	instance=get_object_or_404(Post, id=id)
	instance.delete()
	messages.success(request, "Successfully deleted")
	instance=Post.objects.all()
		context={
			"instance":instance,
			"title":"Index All"
		}
	return render(request, "indexAll.html", context)

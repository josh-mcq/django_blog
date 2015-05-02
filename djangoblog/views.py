from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404

from blog.models import Blog, Category


def home(request):
	return render_to_response('home.html')

def view_post(request, slug):   
	return render_to_response('view_post.html', {
		'post': get_object_or_404(Blog, slug=slug)
	})

def view_category(request, slug):
	category = get_object_or_404(Category, slug=slug)
	return render_to_response('view_category.html', {
	    'category': category,
	    'posts': Blog.objects.filter(category=category)[:5]
	})
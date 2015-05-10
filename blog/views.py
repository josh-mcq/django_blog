from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404

from blog.models import Post, Category



def index(request):
	return render_to_response('index.html', {
		'categories': Category.objects.all(),
		'posts': Post.objects.all()[:5]
	})

def joshmcquiston(request):
	return render_to_response('joshmcquiston.html',
	)

def view_post(request, slug): 
    return render_to_response('view_post.html', {
		'post': get_object_or_404(Post, slug=slug)
	})

def view_category(request, slug):
	category = get_object_or_404(Category, slug=slug)
	return render_to_response('view_category.html', {
		'category' : category,
	    'posts': Post.objects.filter(category=category)[:5]
	})



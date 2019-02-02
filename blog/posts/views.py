from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Post, Category
from .forms import PostForm

class CategoryListMixin:

	def get_context_data(**kwargs):
		context['categories'] = Category.objects.all()


class PostsList(ListView):
    model = Post
    template_name = 'posts/posts_list.html'

    def get_context_data(self, **kwargs):
    	context = super().get_context_data(**kwargs)
    	context['posts_list'] = Post.objects.all()
    	context['categories'] = Category.objects.all()
    	return context

'''class CategoryList(ListView):
    model = Post
    template_name = 'posts/category_list.html'

    def get_context_data(self, **kwargs):
    	context = super().get_context_data(**kwargs)
    	context['categorys_posts'] = Post.objects.all().filter(category__id = category.id)
    	return context'''

def post_detail(request, post_id):

    post = Post.objects.get(id=post_id)
    context = {'post':post}
    return render(request, 'posts/post_detail.html', context)

class CategoryPostsView(ListView, CategoryListMixin):
	model = Post
	template_name = 'posts/category_posts.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['posts_list'] = Post.objects.filter(category__id = self.kwargs['category_id'])
		return context



def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_list')
        else:
        	return render(request, 'posts/add_post.html', {'form': form})

    else:
        form = PostForm()
    return render(request, 'posts/add_post.html', {'form': form})

def post_update(request, post_id):
    post = get_object_or_404(Post, id = post_id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', post_id=post_id)
        else:
        	return render(request, 'posts/update_post.html', {'form': form})
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/update_post.html', {'form': form})

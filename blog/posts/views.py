from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Post, Category


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

class PostDetail(DetailView):

	model = Post
	template_name = 'posts/post_detail.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['posts_list'] = Post.objects.all()
		context['post'] = Post.objects.all().filter(_id = post_id)
		return context

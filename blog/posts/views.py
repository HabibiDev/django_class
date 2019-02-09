from django.shortcuts import render, redirect, get_object_or_404, Http404
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Post, Category
from .forms import PostForm

class CategoryListMixin:

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['categories'] = Category.objects.all()
		return context


class PostsList(CategoryListMixin, ListView):
    model = Post
    template_name = 'posts/post_list.html'

    def get_context_data(self, **kwargs):
    	context = super().get_context_data(**kwargs)
    	context['posts_list'] = Post.objects.select_related('category').all()
    	return context

'''class CategoryList(ListView):
    model = Post
    template_name = 'posts/category_list.html'

    def get_context_data(self, **kwargs):
    	context = super().get_context_data(**kwargs)
    	context['categorys_posts'] = Post.objects.all().filter(category__id = category.id)
    	return context'''
class PostDetailView(CategoryListMixin, DetailView):
	model = Post
	template_name = 'posts/post_detail.html'


	def get_context_data(self, **kwargs):
		cnt = self.request.session.get('cnt', 0)
		cnt+=1
		self.request.session['cnt'] = cnt
		context = super().get_context_data(**kwargs)
		context['post'] = self.get_object()
		context['cnt'] = cnt
		return context



class CategoryPostsView(CategoryListMixin, ListView):
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
            return redirect('posts:post_list')
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
            return redirect('posts:post_detail', post_id=post_id)
        else:
        	return render(request, 'posts/update_post.html', {'form': form})
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/update_post.html', {'form': form})

def login_user(request):
	if request.method == 'POST':
		u = authenticate(username = request.POST['username'],
						 password = request.POST['password'],)
		if u is None:
			raise Http404
		else:
			login(request, u)

	return redirect('/posts/')
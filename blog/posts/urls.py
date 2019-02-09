from django.urls import path
from .views import PostsList, PostDetailView, CategoryPostsView, add_post, post_update, login_user

app_name = 'posts'

urlpatterns = [
    path('', PostsList.as_view(), name = 'post_list'),
    path('<int:pk>', PostDetailView.as_view(), name = 'post_detail'),
    path('category/<int:category_id>', CategoryPostsView.as_view(), name = 'category_posts'),
    path('add_post', add_post, name = 'add_post'),
    path('post_update/<int:post_id>', post_update, name = 'post_update'),
    path('login/', login_user, name = 'login'),

    
]
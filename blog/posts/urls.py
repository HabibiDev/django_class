from django.urls import path
from .views import PostsList, post_detail, CategoryPostsView, add_post, post_update

urlpatterns = [
    path('', PostsList.as_view(), name = 'post_list'),
    path('<int:post_id>', post_detail, name = 'post_detail'),
    path('category/<int:category_id>', CategoryPostsView.as_view(), name = 'category_posts'),
    path('add_post', add_post, name = 'add_post'),
    path('post_update/<int:post_id>', post_update, name = 'post_update'),

    
]
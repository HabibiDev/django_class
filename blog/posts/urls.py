from django.urls import path
from .views import PostsList, PostDetailView, CategoryPostsView, add_post, post_update, login_user
from .api_views import PostListApiView, PostDetailApiView, PostList, PostDetail, CategoryDetail, CategoryList, PostViewSet

app_name = 'posts'

urlpatterns = [
    path('', PostsList.as_view(), name = 'post_list'),
    path('<int:pk>', PostDetailView.as_view(), name = 'post_detail'),
    path('category/<int:category_id>', CategoryPostsView.as_view(), name = 'category_posts'),
    path('add_post', add_post, name = 'add_post'),
    path('post_update/<int:post_id>', post_update, name = 'post_update'),
    path('login/', login_user, name = 'login'),
    path('api_categories/', CategoryList.as_view(), name = 'api_category_list'),
    path('api_categories/<int:pk>', CategoryDetail.as_view(), name = 'api_category_detail'),
    path('api_posts/', PostList.as_view(), name = 'api_post_list'),
    path('api_posts/<int:pk>', PostDetail.as_view(), name = 'api_post_detail'),
    path('api_posts_view/', PostViewSet, name = 'api_post_view_set'),

    
]
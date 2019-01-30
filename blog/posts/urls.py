from django.urls import path
from .views import PostsList, post_detail

urlpatterns = [
    path('', PostsList.as_view()),
    path('<int:post_id>', post_detail, name = 'post_detail')
    #path('<int.category_id>/', CategoryList.as_view(), name = 'category_list')
]
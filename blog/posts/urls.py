from django.urls import path
from .views import PostsList, PostDetail

urlpatterns = [
    path('', PostsList.as_view()),
    path('<int.post_id>/', PostDetail.as_view(), name = 'post_detail')
    #path('<int.category_id>/', CategoryList.as_view(), name = 'category_list')
]
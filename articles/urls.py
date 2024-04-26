from django.urls import path
from .views import PostCreate, PostList, PostDetail

urlpatterns = [
    path('article/', PostCreate.as_view(), name='create_article'),
    path('article/<int:limit>/<int:offset>/', PostList.as_view(), name='list_articles'),
    path('article/<int:pk>/', PostDetail.as_view(), name='detail_article'),
]
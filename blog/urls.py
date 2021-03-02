from django.urls import path
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView


urlpatterns = [
    path('', HomeView.as_view(), name="blog-home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="blog-article-detail"),
    path('add_post/', AddPostView.as_view(), name='home-add-post'),
    path('add_category/', AddCategoryView.as_view(), name='home-add-category'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'),
    path('category/<str:cats>/', CategoryView, name='category'),
]

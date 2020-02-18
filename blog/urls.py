from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('blog_list/', views.BlogListView.as_view(), name="blog_list"),
    path('blog_detail/<int:pk>/', views.BlogDetailView.as_view(), name="blog_detail"),
    path('atcoder/', views.AtcoderView.as_view(), name="atcoder")
]
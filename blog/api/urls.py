from django.urls import path

from blog.api import views

app_name = 'blog'


urlpatterns = [
    path('<slug>/', views.api_detail_blog_view, name="detailapi"),
    path('<slug>/update/', views.api_update_blog_view, name="updateapi"),
    path('<slug>/delete/', views.api_delete_blog_view, name="deleteapi"),
    path('create', views.api_create_blog_view, name="createapi"),
]

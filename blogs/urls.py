from django.urls import path
from . import views
urlpatterns = [
    path('', views.showblogs, name='show_blogs'),
    path('add_blog/',views.add_blog, name='add_blog'),
    path('edit-blog/<int:blog_id>/', views.edit_blog, name='edit_blog'),
    path('delete-blog/<int:blog_id>/', views.delete_blog, name='delete_blog'),
]

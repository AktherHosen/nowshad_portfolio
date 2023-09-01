from django.urls import path
from . import views
urlpatterns = [
    path('', views.showblogs, name='show_blogs'),
    path('add_blog/',views.add_blog, name='add_blog'),
]

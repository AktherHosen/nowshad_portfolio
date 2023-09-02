from django.urls import path
from . import views
urlpatterns = [
    path('signin/',views.user_login, name='signin'),
    path('register/',views.register, name='register'),
    path('profile/',views.profile, name='profile'),
    path('logout/',views.user_logout, name='logout'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('add_skill/', views.add_skill, name='add_skill'),
    path('show_skills/', views.show_skills, name='show_skills'),
    path('edit_skill/<int:skill_id>/', views.edit_skill, name='edit_skill'),
]

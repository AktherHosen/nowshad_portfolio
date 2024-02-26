from django.urls import path
from . import views
urlpatterns = [
    path('signin/',views.user_login, name='signin'),
    path('register/',views.register, name='register'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('logout/',views.user_logout, name='logout'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('add_skill/', views.add_skill, name='add_skill'),
    path('show_skills/', views.show_skills, name='show_skills'),
    path('edit_skill/<int:skill_id>/', views.edit_skill, name='edit_skill'),
    path('delete_skill/<int:skill_id>/', views.delete_skill, name='delete_skill'),
    path('messages/', views.all_messages, name='messages'),
    path('delete_message/<int:message_id>/', views.delete_message, name='delete_message'),
    path('upload_resume/',views.upload_resume, name='upload_resume'),
]

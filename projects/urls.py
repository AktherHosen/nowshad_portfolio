from django.urls import path
from . import views
urlpatterns = [
    path('',views.portfolio_project, name='projects'),
    path('dashboard_project',views.dashboard_project, name='dashboard_project'),
    path('add_project/',views.add_project, name='add_project'),
    path('<int:project_id>',views.portfolio_project_details, name='details'),
    path('review/<int:project_id>/create',views.create_review, name='create_review'),
    path('edit_project/<int:project_id>/', views.edit_project, name='edit_project'),
    path('delete_project/<int:project_id>/', views.delete_project, name='delete_project'),
    path('delete_review/<int:review_id>/', views.delete_review, name='delete_review'),
]

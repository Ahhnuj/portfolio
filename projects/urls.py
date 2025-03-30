from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('project/<slug:slug>/', views.project_detail, name='project_detail'),
    path('project/new/', views.project_new, name='project_new'),
    path('project/<slug:slug>/edit/', views.project_edit, name='project_edit'),
    path('project/<slug:slug>/delete/', views.project_delete, name='project_delete'),
    path('tag/<slug:tag_slug>/', views.project_list, name='project_list_by_tag'),
] 
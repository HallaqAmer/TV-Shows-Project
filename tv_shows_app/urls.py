from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('shows', views.display_shows),
    path('shows/new', views.new_show, name="new"),
    path('shows/create', views.create_new_show, name="create"),
    path('shows/<int:showid>', views.display_show_info, name="info"),
    path('shows/edit/<int:showid>/', views.display_show_edit, name="edit"),
    path('shows/<int:showid>/update', views.update_show, name="update"),
    path('shows/destroy', views.delete_show, name="destroy"),
    
]

from django.urls import path
from . import views
from music.views import delete_file

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('upload/', views.upload, name='upload'),
    path('delete/<int:file_id>/', delete_file, name='delete_file'),
    path('my_files/', views.my_files, name='my_files'),
    path('delete-file/<int:file_id>/', views.delete_file, name='delete_file'),
]

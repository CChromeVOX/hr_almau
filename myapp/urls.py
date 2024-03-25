from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),  
    path('main/', views.main, name='main'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('register/', views.register, name='register'),
    path('accounts/profile/', views.profile, name='profile'),
    path('accounts/edit_profile/', views.edit_profile, name='edit_profile'),
    path('accounts/edit_project/<int:pk>/', views.edit_project, name='edit_project'),  # URL для редактирования проекта
    path('accounts/delete_project/<int:pk>/', views.delete_project, name='delete_project'), 
    path('search_user/', views.search_user, name='search_user'),
    path('resume/<int:user_id>/', views.resume, name='resume'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

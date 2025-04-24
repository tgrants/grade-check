from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
	path('', views.home, name='home'),
	path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),
	path('profile/', views.profile_view, name='profile'),
	path('password_change/', auth_views.PasswordChangeView.as_view(template_name='password_change.html'), name='password_change'),
	path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'), name='password_change_done'),
]

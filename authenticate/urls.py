from django.urls import path, re_path
from authenticate import views as views
from authenticate import dropbox_views
from authenticate import googledrive_views
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('', views.index,name='index'),
	path('home/',views.index,name='index'),
	path('signup/', views.signup, name='signup'),
	path('logout/', views.log_out, name='logout'), # need to create
	# path('login', auth_views.LoginView.as_view(), name='login')
	path('login/', views.log_in,name='login'),

	# Dropbox views
	path('dropbox/redirect/', dropbox_views.redirect_away, name="dropbox_redirect"),
	path('dropbox/save_token/', dropbox_views.save_token,name="dropbox_save_token"),
	path('dropbox/list_folder/', dropbox_views.list_folder, name='dropbox_list_folder'),
	path('dropbox/update_local/', dropbox_views.update_local, name='dropbox_update_local'),
	path('dropbox/update_remote/', dropbox_views.update_remote, name='dropbox_update_remote'),

	# Google Drive views
	path('googledrive/redirect/', googledrive_views.redirect_away, name='googledrive_redirect'),
	path('googledrive/code/', googledrive_views.code, name='googledrive_code'),

]
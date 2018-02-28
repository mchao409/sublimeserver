from django.urls import path, re_path
from authenticate import views as views
from authenticate import dropbox_views
from authenticate import googledrive_views
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('', views.index,name='index'),
	re_path('home/?',views.index,name='index'),
	re_path('signup/?', views.signup, name='signup'),
	re_path('logout/?', views.log_out, name='logout'), # need to create
	# path('login', auth_views.LoginView.as_view(), name='login')
	path('login', views.log_in,name='login'),

	# Dropbox views
	re_path('dropbox/redirect/?', dropbox_views.redirect_away, name="dropbox_redirect"),
	re_path('dropbox/save_token/?', dropbox_views.save_token,name="dropbox_save_token"),
	re_path('dropbox/list_folder/?', dropbox_views.list_folder, name='dropbox_list_folder'),
	re_path('dropbox/update_local/?', dropbox_views.update_local, name='dropbox_update_local'),
	re_path('dropbox/update_remote/?', dropbox_views.update_remote, name='dropbox_update_remote'),

	# Google Drive views
	re_path('googledrive/redirect/?', googledrive_views.redirect_away, name='googledrive_redirect'),
	re_path('googledrive/code/?', googledrive_views.code, name='googledrive_code'),
	re_path('googledrive/gettoken/?', googledrive_views.get_new_token, name='googledrive_gettoken'),
	re_path('googledrive/list_folder/?', googledrive_views.list_folder, name='googledrive_list_folder'),
	re_path('googledrive/update_local/?', googledrive_views.update_local, name='googledrive_list_folder'),
	re_path('googledrive/update_remote/?', googledrive_views.update_remote, name='googledrive_update_remote'),

]
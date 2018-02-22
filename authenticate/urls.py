from django.urls import path, re_path
from authenticate import views as views
from authenticate import dropbox_views
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('', views.index,name='index'),
	path('home/',views.index,name='index'),
	path('redirect/', views.redirect_away, name="redirect_away"),
	path('save_token/', views.save_token,name="save_token"),
	path('signup/', views.signup, name='signup'),
	path('page/', views.go_to_page, name='go_to_page'),
	path('update/', views.update_profile,name='update'), # remove?
	path('logout/', views.log_out, name='logout'), # need to create
	# path('login', auth_views.LoginView.as_view(), name='login')
	path('login/', views.log_in,name='login'),

	# Dropbox views
	path('dropbox/list_folder', dropbox_views.list_folder, name='dropbox_list_folder'),
	path('dropbox/update_local', dropbox_views.update_local, name='dropbox_update_local'),
	path('dropbox/update_remote', dropbox_views.update_remote, name='dropbox_update_remote'),

]
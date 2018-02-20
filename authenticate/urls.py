from django.urls import path
from authenticate import views as views
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('', views.index,name='index'),
	path('home',views.index,name='index'),
	path('redirect/', views.redirect_away, name="redirect_away"),
	path('save_token/', views.save_token,name="save_token"),
	path('signup/', views.signup, name='signup'),
	path('page', views.go_to_page, name='go_to_page'),
	path('update', views.update_profile,name='update'), # remove?
	path('logout', views.log_out, name='logout'), # need to create
	path('login', auth_views.LoginView.as_view(), name='login')
]
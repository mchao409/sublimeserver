from django.urls import path
from authenticate import views as views

urlpatterns = [
	path('',views.index,name='index'),
	path('redirect/', views.redirect_away, name="redirect_away"),
	path('save_token/', views.save_token,name="save_token"),
	path('signup/', views.signup, name='signup'),
	path('page', views.go_to_page, name='go_to_page')
	# path('finish', views.finish)


]
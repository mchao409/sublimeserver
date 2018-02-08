from django.urls import path
from . import views


urlpatterns = [
	path('',views.index,name='index'),
	path('redirect/', views.redirect_away, name="redirect_away"),
	path('save_token/', views.save_token,name="save_token")
	# path('finish', views.finish)


]
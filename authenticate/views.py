from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
# from django.contrib.sessions.models import Session
# from django.contrib.sessions.backends.db import SessionStore
from django.contrib.auth.models import User
from django.contrib import messages
from authenticate.models import Profile
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
import os.path
import os
import requests

def signup(request):
	if request.method == 'POST':
		print("here")
		form = UserCreationForm(request.POST)
		print(form)
		if form.is_valid():
			user = form.save()
			login(request,user)
			print("valid form")
			return render(request,'home.html')
	return render(request, 'signup.html', {'form': UserCreationForm()})

def log_out(request):
	logout(request)
	return render(request,'home.html')

def index(request):
	return render(request,'home.html')

# User first accesses localhost:8000/redirect
# They go to the dropbox place for authorization
def redirect_away(request):
	print("hello")
	APP_KEY = os.environ["DROPBOX_KEY"]
	# return redirect("https://google.com")
	# print(APP_KEY)

	# return redirect("https://www.dropbox.com/oauth2/authorize?client_id=" + APP_KEY + 
	#   "&response_type=code&redirect_uri=http://localhost:5000/save_token")
	return redirect("https://www.dropbox.com/oauth2/authorize?client_id=" + APP_KEY + 
	  "&response_type=code&redirect_uri=http://localhost:8000/save_token")
	print(APP_KEY)
	return redirect("https://www.dropbox.com/oauth2/authorize?client_id=" + APP_KEY + 
	  "&response_type=code&redirect_uri=https://pure-sands-96563.herokuapp.com/save_token")

# User is redirected by Dropbox to localhost:8000/save_token/?code=blahblah
def save_token(request):
	code = request.GET.get("code", "")
	if code == "":
		return HttpResponse("Unsuccessful Authorization. Please Try Again")
	# f = open('~/Desktop/CSC-630/open-source/sublimeserver/authenticate/app_info.txt')
	print(code)
	APP_KEY = os.environ["DROPBOX_KEY"]
	APP_SECRET = os.environ["DROPBOX_SECRET"]
	head = {"code": code,
			"grant_type": "authorization_code",
			 "client_id": APP_KEY,
			"client_secret": APP_SECRET,
			# "redirect_uri": "http://localhost:5000/save_token"}

			"redirect_uri": "http://localhost:8000/save_token"}
			# "redirect_uri": "https://pure-sands-96563.herokuapp.com/save_token"}
	r = requests.post("https://api.dropboxapi.com/oauth2/token", head)
	token_json = r.json()
	print(token_json)
	token = token_json["access_token"]
	if Profile.objects.filter(user=request.user).exists():
		request.user.profile.dropbox_token = token
		request.user.profile.save()
	else:
		profile = Profile.objects.create(user=request.user)
		request.user.profile.dropbox_token = token
		request.user.profile.save()
	return HttpResponse("You have been successfully authenticated to Dropbox")

def go_to_page(request):
	return render(request, 'dropbox_saving.html')

def update_profile(request):
	if request.user.profile:
		request.user.profile.year = "henfjwefnewj"
		request.user.profile.save()

	# profile = Profile.objects.create(user=request.user)
	# user_id = request.user.id
	# user = User.objects.get(pk=user_id)
	# request.user.profile.bio = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit...'
	# request.user.profile.save()
	return HttpResponse(request.user.profile.year)









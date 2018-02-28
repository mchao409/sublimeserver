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
			return render(request,'home.html')
	return render(request, 'signup.html', {'form': UserCreationForm()})

def log_in(request):
	if request.POST:
		username = request.POST['username']
		password = request.POST['password']
		print("username: " + username + " password: " + password)
		user = authenticate(username=username, password=password)
		print(user)
		if user is not None and user != "None":
			login(request,user)
			return redirect("index")
		else:
			return HttpResponse("Error, please try again")
	return render(request,"registration/login.html", {'form': AuthenticationForm()})

def log_out(request):
	logout(request)
	return redirect("index")

def index(request):
	return render(request,'home.html')









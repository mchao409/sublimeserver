from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.sessions.models import Session
from django.contrib.sessions.backends.db import SessionStore
import os.path
import os
import requests


def index(request):
	return HttpResponse("Sublime-Text-Sync")

# User first accesses localhost:8000/redirect
# They go to the dropbox place for authorization
def redirect_away(request):
	APP_KEY = os.environ["DROPBOX_KEY"]
	# return redirect("https://google.com")
	# print(APP_KEY)

	# return redirect("https://www.dropbox.com/oauth2/authorize?client_id=" + APP_KEY + 
	#   "&response_type=code&redirect_uri=http://localhost:5000/save_token")
	# return redirect("https://www.dropbox.com/oauth2/authorize?client_id=" + APP_KEY + 
	#   "&response_type=code&redirect_uri=http://localhost:8000/save_token")
	print(APP_KEY)
	return redirect("https://www.dropbox.com/oauth2/authorize?client_id=" + APP_KEY + 
	  "&response_type=code&redirect_uri=https://pure-sands-96563.herokuapp.com/save_token")

# User is redirected by Dropbox to localhost:8000/save_token/?code=blahblah
def save_token(request):
	print("hellohjdssjd")
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

			# "redirect_uri": "http://localhost:8000/save_token"}
			"redirect_uri": "https://pure-sands-96563.herokuapp.com/save_token"}
	r = requests.post("https://api.dropboxapi.com/oauth2/token", head)
	token_json = r.json()
	print(token_json)
	token = token_json["access_token"]
	r = requests.get("http://localhost:8001/?token=" + token)
	return HttpResponse("Success!")














from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.sessions.models import Session
from django.contrib.sessions.backends.db import SessionStore
import os.path
from dropbox import DropboxOAuth2Flow
import requests


# def get_dropbox_auth_flow(web_app_session):
# 	redirect_uri = "http:localhost:8000/finish"



def index(request):
	if not hasattr(request,"session_key") and request.GET.get("code", "") == "":
		# This is the session you want to save to
		print("NO KEY")
		request.session["has_session"] = True
		request.session["token"] = "NO TOKEN"
		request.session.modified = True
		request.session.save()
	print("GET REQUEST")
	print(request.META)
	print(request.session.session_key)
	# print(request.session.name)
	# request.session["has_session"] = True
	# request.session.save()
	print(request.session.session_key)
	return HttpResponse("hi")

# User first accesses localhost:8000/redirect
# They go to the dropbox place for authorization
def redirect_away(request):
	BASE = os.path.dirname(os.path.abspath(__file__))
	f = open('/Users/michellec/Desktop/CSC-630/Open-Source/sublimeserver/authenticate/app_info.txt')
	APP_KEY = f.readline().rstrip().replace("app key ", "")
	f.close()
	# return redirect("https://google.com")
	# print(APP_KEY)
	return redirect("https://www.dropbox.com/oauth2/authorize?client_id=" + APP_KEY + 
	  "&response_type=code&redirect_uri=http://localhost:8000/save_token")

# User is redirected by Dropbox to localhost:8000/save_token/?code=blahblah
def save_token(request):
	code = request.GET.get("code", "")
	if code == "":
		return HttpResponse("Unsuccessful Authorization. Please Try Again")
	# f = open('~/Desktop/CSC-630/open-source/sublimeserver/authenticate/app_info.txt')
	print(code)
	BASE = os.path.dirname(os.path.abspath(__file__))
	f = open(os.path.join(BASE, "app_info.txt"))
	APP_KEY = f.readline().rstrip().replace("app key ", "")
	APP_SECRET = f.readline().rstrip().replace("secret ", "")
	head = {"code": code,
			"grant_type": "authorization_code",
			 "client_id": APP_KEY,
			"client_secret": APP_SECRET,
			"redirect_uri": "http://localhost:8000/save_token"}
	r = requests.post("https://api.dropboxapi.com/oauth2/token", head)
	token_json = r.json()
	print(token_json)
	token = token_json["access_token"]
	for session in Session.objects.all():
		session_data = SessionStore(session_key=session.session_key)
		if "token" in session_data and session_data["token"] == "NO TOKEN":
			session_data["token"] = token
			session_data.save()
			print(token)
			print("TOKEN SAVED")
			return JsonResponse({"token":token}, safe=False)
	else:
		return HttpResponse("Authorization Failed")













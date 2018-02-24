from django.http import JsonResponse, HttpResponse
from .make_request.DropboxRequest import DropboxRequest
import os
from django.shortcuts import render, redirect
import requests
from authenticate.models import Profile
import datetime

def redirect_away(request):
	client_id = os.environ["GOOGLE_KEY"]
	client_secret = os.environ["GOOGLE_SECRET"]
	scope = 'https://www.googleapis.com/auth/drive'
	redirect_uri ='http://localhost:8000/googledrive/code'
	url =('https://accounts.google.com/o/oauth2/v2/auth?response_type=code' +
		'&client_id={}&redirect_uri={}&scope={}&access_type=offline'.format(client_id,redirect_uri,scope))
	return redirect(url)

def code(request):
	if request.GET.get("error","") != "":
		return redirect("index")
	code = request.GET.get("code", "") + "#"
	print(code)
	data = {
	'code': code,
	'client_id': os.environ["GOOGLE_KEY"],
	'client_secret': os.environ["GOOGLE_SECRET"],
	'redirect_uri': 'http://localhost:8000/googledrive/code',
	'grant_type': 'authorization_code',
	'access_type': 'offline'
	}
	r = requests.post('https://www.googleapis.com/oauth2/v4/token', data=data)
	token = r.json()["access_token"]
	if not Profile.objects.filter(user=request.user).exists():
		profile = Profile.objects.create(user=request.user)
	else:
		profile = request.user.profile
	profile.googledrive_token = token
	if 'refresh_token' in r.json():
		print(r.json()["refresh_token"])
		profile.googledrive_refresh = r.json()["refresh_token"]
	now = datetime.datetime.now()
	d = datetime.timedelta(seconds=40)
	profile.timesaved = now + d
	profile.save()
	print(request.user.profile.googledrive_refresh)
	print(r.json())
	return render(request,"success.html")
	# return (requests.post("https://www.googleapis.com/oauth2/v4/token", head))

def get_new_token(request):
	pass

def save_token(request):
	return HttpResponse(request.POST.get("token", ""))




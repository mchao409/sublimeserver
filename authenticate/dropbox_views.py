from django.http import JsonResponse, HttpResponse
from .make_request.DropboxRequest import DropboxRequest
import os
from django.shortcuts import render, redirect
import requests
from authenticate.models import Profile

# User first accesses localhost:8000/redirect
# They go to the dropbox place for authorization
def redirect_away(request):
	APP_KEY = os.environ["DROPBOX_KEY"]
	# return redirect("https://google.com")

	# return redirect("https://www.dropbox.com/oauth2/authorize?client_id=" + APP_KEY + 
	#   "&response_type=code&redirect_uri=http://localhost:5000/save_token")
	return redirect("https://www.dropbox.com/oauth2/authorize?client_id=" + APP_KEY + 
	  "&response_type=code&redirect_uri=http://localhost:8000/dropbox/save_token")
	# return redirect("https://www.dropbox.com/oauth2/authorize?client_id=" + APP_KEY + 
	  # "&response_type=code&redirect_uri=https://sublimesync.herokuapp.com/save_token")	

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
			"redirect_uri": "http://localhost:8000/dropbox/save_token"}
			# "redirect_uri": "https://sublimesync.herokuapp.com/save_token"}
	r = requests.post("https://api.dropboxapi.com/oauth2/token", head)
	token_json = r.json()
	print(token_json)
	token = token_json["access_token"]
	if Profile.objects.filter(user=request.user).exists():
		request.user.profile.dropbox_token = token
		request.user.profile.save()
		print(request.user)
	else:
		profile = Profile.objects.create(user=request.user)
		request.user.profile.dropbox_token = token
		print(request.user)
		request.user.profile.save()
	return render(request,"success.html")

def list_folder(request):
	token = request.user.profile.dropbox_token
	req = DropboxRequest(token)
	return JsonResponse(req.list_folder(),safe=False)

def update_local(request):
	token = request.user.profile.dropbox_token
	req = DropboxRequest(token)
	return HttpResponse(req.download(request.POST["name"]))

def update_remote(request):
	token = request.user.profile.dropbox_token
	req = DropboxRequest(token)
	# print(token)
	# print(request.POST)
	return JsonResponse(req.update_remote(request.POST["name"],request.POST["text"].encode()),safe=False)



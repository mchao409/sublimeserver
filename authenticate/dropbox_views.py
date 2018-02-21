from django.http import JsonResponse, HttpResponse
from .make_request.DropboxRequest import DropboxRequest

def handle_request(request):
	pass

def list_folder(request):
	token = request.user.profile.dropbox_token
	req = DropboxRequest(token)
	return JsonResponse(req.list_folder(),safe=False)

def update_local(request):
	token = request.user.profile.dropbox_token
	
from django.http import JsonResponse, HttpResponse
from .make_request.DropboxRequest import DropboxRequest

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



from django.shortcuts import render
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import ensure_csrf_cookie
from .upload import uploadPhoto, getPhotoDetails, postComment, postLike
from .models import Photo

# Create your views here.
def photos(request):
    return render(request, "photos/photos.html", {})

def upload(request,photo_id):
	response = uploadPhoto(photo_id)
	return render(request, "photos/upload.html", {'response':response})

@ensure_csrf_cookie
def show(request):
	if request.method == 'POST':
		print request.POST
		photo_list = []
		for id in request.POST.getlist('photo_id_list[]'):
			try:
				photo_list.append(Photo.objects.get(pk=id))
			except ObjectDoesNotExist:
				pass
			except Exception , e:
				return JsonResponse({'status':'error', 'message':str(e)})

		#return JsonResponse({'photo_list':request.POST.getlist('photo_id_list')})
		return JsonResponse({'photo_list':[getPhotoDetails(x) for x in photo_list]})
	else:
		photo_id_list = [ x.id for x in Photo.objects.all() ]
		return render(request,"photos/show.html",{'photo_id_list':photo_id_list})

def ajax_post_comment(request):
	access_token = request.POST.get('access_token','')
	photo_id = request.POST.get('photo_id','')
	comment_text = request.POST.get('comment_text','')
	print request.POST
	if access_token == '' or photo_id=='' or comment_text=='':
		return JsonResponse({'status':'error', 'message':'post data missing'})
	else:
		return JsonResponse(postComment(access_token,photo_id,comment_text))

def ajax_post_like(request):
	access_token = request.POST.get('access_token','')
	photo_id = request.POST.get('photo_id','')

	if access_token == '' or photo_id=='':
		return JsonResponse({'status':'error', 'message':'post data missing'})
	else:
		return JsonResponse(postLike(access_token,photo_id))
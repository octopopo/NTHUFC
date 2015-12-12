#-*- encoding=UTF-8 -*-
import flickr_api
import facebook
from .authorization_token import __facebook_page_token, __flickr_api_key, __flickr_api_secret
from .models import Photo

def uploadPhoto(id):
	'''
		先將照片上傳到 Flickr，再張貼到 Facebook。
		Flickr驗證會用到 oauth_verifier.txt ，要放在 NTHUFC 根目錄中
		authorization_token.py 存放 Facebook 和 Flickr 驗證會用到的資訊，不要放到 github 上
	'''
	photo = Photo.objects.get(pk=id)
	photo_file_path = photo.image.url[1:]
	result = {}

	if photo.flickr_photo_id=='':
		flickr_api.set_keys(api_key = __flickr_api_key, api_secret = __flickr_api_secret)
		flickr_api.set_auth_handler('oauth_verifier.txt')
		flickr_response = flickr_api.upload(\
			photo_file = photo_file_path, 
			title =photo.title,
			description = u'地點: '+photo.location_marker.location_text+u'\n拍攝者: '+photo.owner.nickname+'\n\n'+photo.content,
			tags = photo.tags + ' ' + photo.owner.nickname,
			is_public = 1,
			safety_level =1,
			content_type  =1,
			hidden = 1,
		)
		photo.flickr_photo_id = flickr_response.id
		photo_info = flickr_response.getInfo()
		photo.flickr_photo_url = 'https://farm{}.staticflickr.com/{}/{}_{}.jpg'.format(photo_info['farm'], photo_info['server'], flickr_response.id, photo_info['secret'])
		photo.save()
		result['flickr_response'] = flickr_response
	else:
		result['flickr_response'] = 'already upload to flickr'

	if photo.facebook_post_id =='':
		result['facebook_response'] = uploadToFacebook(photo)
	else:
		result['facebook_response'] = updateFlickrPhotoURL(photo)

	return result

def getFacebookPostCntent(photo):
	'''
		產生Facebook的貼文內容
	'''
	label = ' '+photo.tags;
	label = label.replace(' ',' #');
	return u'{} {}\n===================\n地點: #{}\n拍攝者: #{}\n \n{}\n \n原始圖片連結: https://www.flickr.com/photos/138506275@N05/{}'.format(
			photo.title, label, photo.location_marker.location_text, photo.owner.nickname, photo.content, photo.flickr_photo_id)

def uploadToFacebook(photo):
	'''
		將新的照片張貼到Facebook，並把貼文ID存起來
	'''
	graph = facebook.GraphAPI(access_token=__facebook_page_token, version='2.5')
	
	photo_file_path = photo.image.url[1:]
	facebook_response = graph.put_photo(
		image= open(photo_file_path,'rb'), 
		message= getFacebookPostCntent(photo)
	)
	photo.facebook_post_id = facebook_response['post_id']
	photo.save()
	return facebook_response

def updateFlickrPhotoURL(photo):
	'''
		如果該篇照片已經有Facebook貼文的ID，那就更新貼文內容而不要重新張貼
	'''
	graph = facebook.GraphAPI(access_token=__facebook_page_token, version='2.5')
	
	facebook_response = graph.update_photo(
		facebook_post_id=photo.facebook_post_id,
		message= getFacebookPostCntent(photo)
	)
	return facebook_response
from datetime import datetime

import requests
from django.http import JsonResponse,HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.db.models import CharField

from .models import IGUser

# FIXME: Temporarily using csrf_exempt before the access token can be get automatically
@csrf_exempt
def get_token(request):
    access_token = None
    user_id = None
    #-------------------------------------------------
    # TODO: get access token and usert_id live
    try:
        if request.method == 'POST':
            access_token = request.POST['access_token']
            user_id = request.POST['user_id']
    except:
        pass
    #-------------------------------------------------

    if access_token is None or user_id is None:
        return HttpResponse('Unauthorized: no token or user id', status=401)

    # Store token
    try:
        ig_user = IGUser.objects.get(user_id=user_id)
        ig_user.access_token = access_token
        ig_user.save()
    except IGUser.DoesNotExist:
        ig_user = IGUser.objects.create(user_id=user_id, access_token=access_token)

    return HttpResponse(ig_user.id)

# FIXME: Temporarily using csrf_exempt before the access token can be get automatically
@csrf_exempt
def get_media(request, app_user_id):
    ig_user = None
    #-------------------------------------------------
    # TODO: implement proper app user auth
    if request.method == 'POST':
        try:
            ig_user = IGUser.objects.get(pk=app_user_id)
        except IGUser.DoesNotExist:
            pass
    if ig_user is None:
        return HttpResponse('Unauthorized: no ig_user', status=401)
    #-------------------------------------------------
    media_data = request_media(ig_user.access_token)
    if media_data is not None:
        ig_user.media_data = media_data
        ig_user.media_timestamp = datetime.utcnow()
        ig_user.save()
    return JsonResponse({'media_data':media_data})

def request_media(access_token: CharField, number_media: int = 6) -> dict:
    # Get number_media most recent media
    response = requests.get(
        url='https://graph.instagram.com/me/media',
        params={
            'fields': 'id,timestamp,media_type,media_url,thumbnail_url,permalink',
            'access_token': access_token,
        },
    )
    response_json = response.json()
    if 'data' in response_json:
        sorted_media = sorted(
            filter(
                lambda media: media['media_type'] == 'IMAGE'
                or media['media_type'] == 'VIDEO',
                response_json['data'],
            ),
            key=lambda media: media['timestamp'],
            reverse=True,
        )[:number_media]
        sorted_media = list(map(lambda media: [media['media_url'] if media['media_type'] == 'IMAGE' else media['thumbnail_url'], media['permalink']], sorted_media))
        return sorted_media
    return None

def get_widget(request, app_user_id):
    ig_user = None
    #-------------------------------------------------
    # TODO: implement proper app user auth
    try:
        ig_user = IGUser.objects.get(pk=app_user_id)
    except IGUser.DoesNotExist:
        pass
    if ig_user is None:
        return HttpResponse('Unauthorized: no ig_user', status=401)
    #-------------------------------------------------
    media_data = ig_user.media_data
    if media_data is None:
        return HttpResponse('')
    context = {'media_data': media_data}
    return render(request, 'get_widget/index.html', context)

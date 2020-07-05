import requests
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import IGUser

# FIXME: Temporarily using csrf_exempt before the access token can be get automatically
@csrf_exempt
def index(request):
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

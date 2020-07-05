from django.shortcuts import render

import requests
from django.http import HttpResponse
from django.shortcuts import render

from get_token.models import IGUser

def index(request, app_user_id):
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

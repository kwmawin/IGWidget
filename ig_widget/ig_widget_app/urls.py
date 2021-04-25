from django.urls import path

from . import views

urlpatterns = [
    path('ig_auth', views.ig_auth, name='ig_auth'),
    path('get_auth_code', views.get_auth_code, name='get_auth_code'),
    path('get_token_and_user', views.get_token_and_user, name='get_token_and_user'),
    path('get_token', views.get_token, name='get_token'),
    path('get_widget/<int:app_user_id>', views.get_widget, name='get_widget'),
    path('get_media/<int:app_user_id>', views.get_media, name='get_media'),
]

from django.urls import path

from . import views

urlpatterns = [
    path("get_token", views.get_token, name="get_token"),
    path("get_widget/<int:app_user_id>", views.get_widget, name="get_widget"),
    path("get_media/<int:app_user_id>", views.get_media, name="get_media"),
]

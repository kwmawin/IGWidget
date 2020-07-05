from django.urls import path

from . import views

urlpatterns = [path('<int:app_user_id>', views.index, name='index')]

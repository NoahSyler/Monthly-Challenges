from django.urls import path

from . import views

#url config
urlpatterns = [
    path("", views.index),
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name='month-challenge'),
]
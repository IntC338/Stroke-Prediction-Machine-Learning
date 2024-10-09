from django.urls import path
from . import views

urlpatterns = [
    path("", views.stroke_predict, name="stroke_predict"),
]

# detection/urls.py

from django.urls import path
from .views import ObjectDetectionAPI

urlpatterns = [
    path('', ObjectDetectionAPI.as_view(), name='object_detection'),

]
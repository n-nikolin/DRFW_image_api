# from django.conf.urls import include
from django.urls import re_path, include
from rest_framework import routers
from .viewsets import ImageViewSet

# initiate router and register all endpoints
router = routers.DefaultRouter()
router.register('images', ImageViewSet, 'images')

# Wire up our API with our urls
urlpatterns = [
    re_path(r'^', include(router.urls)),
]
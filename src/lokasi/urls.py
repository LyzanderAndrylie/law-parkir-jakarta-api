from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register('lokasi', views.LokasiParkirViewSet, basename='lokasi-parkir')

urlpatterns = [
    path('', include(router.urls)),
]

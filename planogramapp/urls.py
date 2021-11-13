from django.urls import path
from . import views
urlpatterns = [
    path('add', views.planogram_add, name = "planogram-add"),
    path('get', views.planogram_get, name = "planogram-get"),
]

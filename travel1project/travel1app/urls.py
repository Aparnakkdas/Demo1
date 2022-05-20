from django.conf.urls.static import static
from django.urls import path

from travel1project import settings
from .import views

urlpatterns = [
  path('',views.demo,name="demo"),
]

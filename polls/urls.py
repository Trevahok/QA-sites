from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns = [
        path('<department>/', views.test, name='dept'),
        path('<department>/<name>/',views.fac_profile,name='fac'),
        ]

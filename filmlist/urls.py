"""filmlist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import re_path
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from films import views


urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^schema$', views.schema_view),
    re_path(r'^films$', views.FilmList.as_view()),
    re_path(r'^films/(?P<pk>[0-9]+)$', views.FilmDetail.as_view()),
    re_path(r'^films/page(?P<page>[0-9]+)/$', views.FilmList.as_view()),
    re_path(r'(?i)^theaters$', views.TheaterList.as_view()),
    re_path(r'(?i)^theaters/(?P<pk>[0-9]+)$', views.TheaterDetail.as_view()),
    re_path(r'(?i)^genres$', views.GenreList.as_view()),
    re_path(r'(?i)^genres/(?P<pk>[0-9]+)$', views.GenreDetail.as_view()),
    re_path(r'^users/$', views.UserList.as_view()),
    re_path(r'^users/(?P<pk>[0-9]+)$', views.UserDetail.as_view()),
#    re_path(r'^film_title$', views.film_title(request)),
    re_path(r'^titles$', views.film_title),
    # re_path(r'^schema$', schema_title),
]

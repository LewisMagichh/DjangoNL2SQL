"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import search
from . import KVwrite
from . import Evalution
from . import utils
urlpatterns = [
    path('search/',search.search),
    path('search-post/',search.search_post),
    path('infer/',search.inferlist),
    path('KVwrite/writeCorrect/',KVwrite.write_correct),
    path('KVwrite/writeError/',KVwrite.write_error),
    path('evalution/',Evalution.evalution),
    path('',search.index),
    path('index/myaudio/',utils.my_record)
]

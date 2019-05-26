"""mkgDjangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

import mkg_demo.views as mv

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', mv.home_page),
    path('entity_recognition/', mv.entity_recognition),
    path('entity_query/', mv.entity_query),
    path('relation_query/', mv.relation_query),
    path('robot_conversion/', mv.robot_conversion),
    path('mkg_classify/', mv.mkg_classify),
    path('detail/', mv.detail),
]

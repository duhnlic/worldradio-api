"""radioapi URL Configuration

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
from django.urls import path, include
from rest_framework import routers
from radio.views import RadioViewSet

router = routers.DefaultRouter()
router.register(r'radio', RadioViewSet)
# /radio/ get show us all radios in json
# /radio/ post create a new radios and accept json
# /radio/<id> get show us one individual radio
# /radio/<id> put update an individual radio
# /radio/<id> delete an individual radio

urlpatterns = [
        # add all of our router urls
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]

"""doplat URL Configuration

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
from django.urls import path, include, re_path
from .router import DefaultRouter
from app.urls import router as router_app
from authperm.urls import router as router_authperm
from project.urls import router as router_project

router = DefaultRouter()
router.extend(router_app)
router.extend(router_authperm)
router.extend(router_project)

urlpatterns = [
    path('api/o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'^api/', include('authperm.urls')),
    re_path(r'^api/', include('app.urls')),
    re_path(r'^api/', include('project.urls')),
]

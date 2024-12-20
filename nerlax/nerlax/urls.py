"""nerlax URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib.auth.decorators import login_required
from apps.building import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('apps.base.urls', 'base'))),
    path('home/', login_required(views.Home), name='home'),
    path('home_client/', login_required(views.HomeClient), name='home_client'),
    path('home_employee/', login_required(views.HomeEmployee), name='home_employee'),
    path('settings/', include(('apps.settings.urls', 'settings'))),
    path('reports/', include(('apps.reports.urls', 'reports'))),
    path('nerlax/', include(('apps.building.urls', 'nerlax'))),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

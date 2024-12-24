"""
URL configuration for store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
#from main_app import views
from store import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_app.urls', namespace='main_app')),
    path('catalog/', include('products_app.urls', namespace='catalog')),
    path('user/', include('users_app.urls', namespace='user')),
    path('basket/', include('basket_app.urls', namespace='basket')),
    path('orders/', include('orders.urls', namespace='orders')),
    # path('pharmacy/', include('pharmacy.urls', namespace='pharmacy')),
    path("__debug__/", include("debug_toolbar.urls")), #DEBUG режим
    #static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
]

if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
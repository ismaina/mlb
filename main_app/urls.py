"""main_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from .sitemaps import ProductSitemap
from django.conf import settings

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path("", include("core_apps.frontend.urls", namespace="frontend")),
    path("products/", include("core_apps.products.urls", namespace='products')),
    path("__reload__/", include("django_browser_reload.urls")),
    path('captcha/', include('captcha.urls')),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": {"products": ProductSitemap}},
    ),
    # static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if bool(settings.DEBUG):
    urlpatterns += path('__debug__/', include('debug_toolbar.urls')),
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "Mill Bakers Admin"

admin.site.site_title = "Mill Bakers Admin Portal"

admin.site.index_title = "Welcome to Mill Bakers portal"
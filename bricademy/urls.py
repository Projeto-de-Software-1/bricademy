
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import home
from users import urls as users_urls
from materials import urls as materials_urls
from ads import urls as ads_urls
urlpatterns = [
    path('', home, name="home"),
    path('materials/', include(materials_urls)),
    path('users/', include(users_urls)),
    path('ads/', include(ads_urls)),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from Profile.views import ProfileRegisterView, ProfileLoginView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('Order/', include('Order.urls')),
    path('Product/', include('Product.urls')),

    path('profile/register', ProfileRegisterView.as_view()),
    path('profile/login', ProfileLoginView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

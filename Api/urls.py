
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import Check,Filesummary
urlpatterns = [
    path('', Check.as_view(), name='Checkpass'),
    path('api/Filesummary', Filesummary.as_view(), name='Filesummary'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from courses.views import home, regenerative_movement_course

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('regenerative-movement-course/', regenerative_movement_course, name='regenerative_movement_course'),
    path('courses/', include('courses.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
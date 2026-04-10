from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from portfolio_backend import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('admin/', admin.site.urls),
    path('api/projects/', include('projects.urls')),
    path('api/blogs/', include('blogs.urls')),
    path('api/auth/', include('authentication.urls')),
    path('api/contacts/', include('contacts.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

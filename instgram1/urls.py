from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^users/', include('users.urls', namespace='users')),

    url(r'', include('inst.urls', namespace='inst')),

    url(r'^chaining/', include('smart_selects.urls')),

    # url(r'^api/', include('rest_framework.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

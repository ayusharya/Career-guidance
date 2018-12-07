from django.conf.urls import url,include
from django.contrib import admin
from.import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ourpage/',include('ourpage.urls')),
    
    url(r'^Resister/',include('Resister.urls')),
    url(r'^Resister2/',include('Resister2.urls')),
    url(r'^table/',include('table.urls')),
    url(r'^about/',include('about.urls')),
]

urlpatterns += staticfiles_urlpatterns()

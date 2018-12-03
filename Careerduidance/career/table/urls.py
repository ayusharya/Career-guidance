from django.conf.urls import url

from.import views

urlpatterns = [
    url(r'^$',views.table11),
    url(r'^table12/',views.table22),
    url(r'^table13/',views.table33),
]

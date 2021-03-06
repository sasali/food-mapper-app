from django.conf.urls import patterns, url, include
from frontend import views
from django.views.generic import TemplateView


print views

urlpatterns = patterns('',
    url(r'^$', 'frontend.views.index'),
    url(r'^login', 'frontend.views.login'),
    url(r'^maps/add', 'frontend.views.addmap'),
    url(r'^maps', 'frontend.views.maps'),
    url(r'^map/(?P<slug>[-\w]+)','frontend.views.map'),
    url(r'^user/(?P<username>[-\w]+)/maps','frontend.views.usermaps'),
    url(r'^user/(?P<username>[-\w]+)','frontend.views.user'),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
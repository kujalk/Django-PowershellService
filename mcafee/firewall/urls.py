from django.conf.urls import url 
from firewall import views 
 
urlpatterns = [ 
    url(r'^api/firewall$', views.firewall_status),
    url(r'^api/firewall/(?P<pk>[0-9]+)$', views.firewall_service),
    url(r'^api/firewall/published$', views.firewall_detail)
]
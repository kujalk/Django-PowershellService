from django.conf.urls import url 
from firewall import views 
 
urlpatterns = [ 
    url(r'^api/firewall$', views.service.as_view()),
]
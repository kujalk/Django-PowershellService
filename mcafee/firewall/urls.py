from firewall import views 
from django.urls import path
 
urlpatterns = [ 
    path('api/firewall/', views.service.as_view()),
    path('api/<slug:servicename>/<slug:status>/',views.servicelist.as_view())
]
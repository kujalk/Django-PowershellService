from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework.response import Response
from rest_framework import status

from firewall.models import firewallstatus
from firewall.serializers import firewallserializer
from rest_framework.generics import ListCreateAPIView
# Create your views here.

class service(ListCreateAPIView):
    queryset=firewallstatus.objects.all()
    serializer_class=firewallserializer

    def create(self,request,*args,**kwargs):
        serializer=self.get_serializer(data=request.data,many=True)
        serializer.is_valid(raise_exception=True)
        try:
            self.perform_create(serializer)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'message':'Problem in creating new item. '+str(e)},status=status.HTTP_400_BAD_REQUEST)

def status_check(request):
    fwdata=firewallstatus.objects.all()
    context={'allstatus':fwdata}

    return render(request, 'service_status.html', context)

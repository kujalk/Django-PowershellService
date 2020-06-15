from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from firewall.models import firewallstatus
from firewall.serializers import firewallserializer
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET', 'POST', 'DELETE'])
def firewall_status(request):
    if request.method == 'GET':
        services = firewallstatus.objects.all()
        
        Date = request.query_params.get('Date', None)
        if Date is not None:
            services = services.filter(Date__icontains=Date)
        
        firewall_serializer = firewallserializer(services, many=True)
        return JsonResponse(firewall_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        firewall_data = JSONParser().parse(request)
        firewall_serializer = firewallserializer(data=firewall_data, many=True)

        if firewall_serializer.is_valid():
            firewall_serializer.save()
            return JsonResponse(firewall_serializer.data, status=status.HTTP_201_CREATED,safe=False) 

        return JsonResponse(firewall_serializer.errors, status=status.HTTP_400_BAD_REQUEST,safe=False)

    elif request.method == 'DELETE':
        count = firewallstatus.objects.all().delete()
        return JsonResponse({'message': '{} Service Status were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
@api_view(['GET', 'PUT', 'DELETE'])
def firewall_service(request, pk):
    try: 
        service = firewallstatus.objects.get(pk=pk) 
    except firewallstatus.DoesNotExist: 
        return JsonResponse({'message': 'The Service Status does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        firewall_serializer = firewallserializer(service) 
        return JsonResponse(firewall_serializer.data) 
 
    elif request.method == 'PUT': 
        service_data = JSONParser().parse(request) 
        firewall_serializer = firewallserializer(service, data=service_data) 
        if firewall_serializer.is_valid(): 
            firewall_serializer.save() 
            return JsonResponse(firewall_serializer.data) 
        return JsonResponse(firewall_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        service.delete() 
        return JsonResponse({'message': 'Service Status was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET'])
def firewall_detail(request):
    service = firewallstatus.objects.filter(Status="Running")
        
    if request.method == 'GET': 
        firewall_serializer = firewallserializer(service, many=True)
        return JsonResponse(firewall_serializer.data, safe=False)

def status_check(request):
    fwdata=firewallstatus.objects.all()
    context={'allstatus':fwdata}

    return render(request, 'service_status.html', context)

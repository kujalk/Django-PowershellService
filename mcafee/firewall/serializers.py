from rest_framework import serializers 
from .models import firewallstatus

class firewallserializer(serializers.ModelSerializer):
    class Meta:
        model=firewallstatus
        fields=('Date',
                'Service_Name',
                'Display_Name',
                'Status'
        )
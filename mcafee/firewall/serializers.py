from rest_framework import serializers 
from .models import firewallstatus

class firewallserializer(serializers.ModelSerializer):
    class Meta:
        model=firewallstatus
        fields='__all__'

        
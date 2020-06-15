from rest_framework import serializers 
from .models import firewallstatus

class Bulkstatusserializer(serializers.ListSerializer):

    def create(self,validated_data):
        status_data=[firewallstatus(**item) for item in validated_data]
        return firewallstatus.objects.bulk_create(status_data)

class firewallserializer(serializers.ModelSerializer):
    class Meta:
        model=firewallstatus
        fields='__all__'
        list_serializer_class=Bulkstatusserializer

        
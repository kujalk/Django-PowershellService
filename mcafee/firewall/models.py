from django.db import models

# Create your models here.
class firewallstatus(models.Model):
    Date=models.CharField(max_length=30)
    Service_Name=models.CharField(max_length=50)
    Display_Name=models.CharField(max_length=50)
    Status=models.CharField(max_length=20)

    def __str__(self):
        return (str(self.pk)+"_"+self.Date)


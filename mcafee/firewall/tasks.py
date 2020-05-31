import datetime
import celery
import subprocess,sys
from celery import shared_task 
from celery import task 

#@celery.decorators.periodic_task(run_every=datetime.timedelta(minutes=1)) # here we assume we want it to be run every 5 mins
@shared_task 
def myTask():
    fileName = "D:\\Django_Dev\\api-powershell\\mcafee\\api-post.log"
    with open(fileName, "w+") as f:
        execute=subprocess.Popen(["powershell.exe","D:\\Django_Dev\\api-powershell\\mcafee\\Get-Service.ps1"],stdout=f)
        execute.communicate()
    print('Hello Works')
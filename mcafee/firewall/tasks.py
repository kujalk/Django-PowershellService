import datetime
import celery
import subprocess.sys

@celery.decorators.periodic_task(run_every=datetime.timedelta(minutes=1)) # here we assume we want it to be run every 5 mins
def myTask():
    execute=subprocess.Popen(["powershell.exe","D:\\Django_Dev\\api-powershell\\mcafee\\Get-Service.ps1"],stdout=sys.stdout)
    execute.communicate()
    
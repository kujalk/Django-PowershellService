from apscheduler.schedulers.background import BackgroundScheduler
from updateservice import update

def start():
    scheduler=BackgroundScheduler()
    scheduler.add_job(update.execute_powershell,'interval',minutes=1)
    scheduler.start()
import datetime
import celery

@celery.decorators.periodic_task(run_every=datetime.timedelta(minutes=1)) # here we assume we want it to be run every 5 mins
def myTask():
    
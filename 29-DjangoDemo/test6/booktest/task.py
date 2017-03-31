import time
from celery import task


@task
def sayhello():
    print 'hello'
    time.sleep(3)
    print 'world'

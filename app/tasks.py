from celery import Celery, current_task
from celery.result import AsyncResult

import json
import numpy as np
import os
import time

BROKER_URL = 'amqp://admin:Ntcn0dsq@rabbit//'
REDIS_URL = 'redis://redis:6379/0'

CELERY = Celery('tasks', broker=BROKER_URL, backend=REDIS_URL)

CELERY.conf.accept_content = ['json', 'msgpack']
CELERY.conf.result_serializer = 'msgpack'

def get_job(job_id):

    return AsyncResult(job_id, app=CELERY)

@CELERY.task()
def do_large_task(num):
    time.sleep(30)
    num = int(num)
    return json.dumps(np.random.rand(num * num).reshape(num, num).tolist())
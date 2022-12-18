import os
import time
import requests
import json
from celery import Celery, chain, Signature


CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://localhost:6379'),
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', 'redis://localhost:6379')

celery = Celery('tasks', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)

@celery.task(name='tasks.revokeall')
def revoke_all():
	# change the url if the name of your monitor container is named differently
	r = requests.get('http://http_revoke-monitor-1:5555/api/tasks') 
	r_dict = json.loads(r.text)
	for task_id in r_dict.keys():
		if r_dict[task_id]["name"] != "tasks.revokeall":
			celery.control.revoke(task_id, terminate=True)

@celery.task(name='tasks.sub_task')
def sub_task(t):
    time.sleep(t)  

@celery.task(name='tasks.main_task')
def main_task(t):
	chained_tasks = chain([
		Signature('tasks.revokeall', args=[], kwargs={}, immutable=True),
		Signature('tasks.sub_task', args=[t], kwargs={}, immutable=True),
	])
	chained_tasks.apply_async()


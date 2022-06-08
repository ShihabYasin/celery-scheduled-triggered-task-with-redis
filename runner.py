import datetime
from celery import Celery

REDIS_BASE_URL = 'redis://localhost:6379'
ScheduledTaskCount = 0
TriggeredTaskCount = 0

app = Celery (
    'runner',
    broker=f"{REDIS_BASE_URL}/0",
    backend=f"{REDIS_BASE_URL}/1"
    )

app.conf.beat_schedule = {
    'scheduled_task': {
        'task': 'runner.scheduled_task',
        'schedule': 5.0,  # Runs in every 5 seconds
        # 'schedule': crontab(minute=5) # Runs in every 5 minutes
        # 'args': (arg_1, arg_2, ...), # Run the function with arguments
        },
    }


@app.task (name="runner.scheduled_task")
def scheduled_task():
    global ScheduledTaskCount
    ScheduledTaskCount += 1
    print (f"Executing your scheduled task. Number of times executes: {ScheduledTaskCount}")
    return {
        "scheduled_task_res": "Success"
        }


@app.task (name='runner.triggered_task', default_retry_delay=200, max_retry=5, soft_time_limit=30)
def triggered_task(current_datetime: datetime):
    global TriggeredTaskCount
    TriggeredTaskCount += 1
    print (f"{str (current_datetime)} Executing your triggered task. Number of times executes: {TriggeredTaskCount}")
    return {
        "triggeredTaskCount_task_res": "Success"
        }

# celery-scheduled-triggered-task-with-redis
Basic app to show celery scheduled task and triggered task with redis broker.



# Simple Task Queue with Celery and Redis (Scheduled & Triggered)


## How to run:
1. Start redis: ```docker run -p 6379:6379 redis:alpine``` in a terminal.
2. Run Celery worker: ```celery --app=runner worker --loglevel=info``` in another terminal.
3. Run: ```celery --app=runner beat --loglevel=info``` for Scheduled Task in another terminal.
or, Run: ```python3 trigger.py``` to simulate Triggered task in another terminal.

For detail, see ```runner.py, trigger.py```.


### Best Practices Check List:
1. Use least arguments as possible. Stateless tasks are better.
2. Set time limits to tasks. CELERYD_TASK_SOFT_TIME_LIMIT
3. Don’t trust broker for security.
4. Be aware of the limits of connection pool limits.


### Ref:
<ul>
<li><a href="https://docs.celeryproject.org/en/stable/userguide/security.html#security">Secure Celery</a> (Celery official docs.)</li>
<li><a href="https://docs.sentry.io/platforms/python/guides/celery/">Integrate Sentry to Celery</a></li>
<li><a href="https://redis.io/topics/security">Secure Redis</a> (Redis official docs.)</li>
<li><a href="https://redis.io/topics/lru-cache#eviction-policies">Eviction Policy on Redis</a> (Redis official docs.)</li>
<li><a href="https://docs.celeryproject.org/en/latest/userguide/monitoring.html#flower-real-time-celery-web-monitor">Monitoring Celery Workers</a> (Celery official docs.)</li>

</ul>
import os
from celery import Celery
from celery.schedules import crontab
os.environ.setdefault('DJANGO_SETTINGS_MODULE', "mysite.settings")

app= Celery('proj')
app.config_from_object('django.conf.settings', namespace='CELERY')
app.autodiscover_tasks()
app.conf.beat_schedule = {
 'run-me-every-ten-seconds': {
 'task': 'movie_auth.tasks.change_flag',
 'schedule': crontab(hour=7, minute=0),
 'args' :(16, 16)}}


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

# table_proj.celery.py
import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'table_proj.settings')

app = Celery('My_first')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')
#app.conf.database_engine_options = {'echo': True}

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
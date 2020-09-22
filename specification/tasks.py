# specification.tasks.py
from celery import shared_task
from celery.task import periodic_task
from celery.schedules import crontab
from datetime import timedelta
#from demoapp.models import Widget


@periodic_task(run_every=(timedelta(seconds=5)), name='my_first_task')
def my_first_task():
    print('Message from FIRST task!!!')

@shared_task
def my_second_task():
    print('Message from SECOND task!!!')

@shared_task
def my_third_task():
    print('Message from THIRD task!!!')


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


# @shared_task
# def count_widgets():
#     return Widget.objects.count()


# @shared_task
# def rename_widget(widget_id, name):
#     w = Widget.objects.get(id=widget_id)
#     w.name = name
#     w.save()
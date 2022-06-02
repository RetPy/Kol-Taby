# import os
#
# from celery import Celery
# from celery.schedules import crontab
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
#
# app = Celery('core')
#
# app.config_from_object('django.conf:settings', namespace='CELERY')
# app.autodiscover_tasks()
#
# app.conf.beat_schedule = {
#     'auto-delete-every-minute': {
#         'task': 'core.tasks.auto_delete',
#         'schedule': crontab(minute=0, hour=0),
#     }
# }
# app.conf.timezone = 'Asia/Bishkek'

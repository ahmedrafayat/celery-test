from celery import Celery

app = Celery('tasks', broker='amqp://127.0.0.1:5672', backend='redis://127.0.0.1:6379/0')
app.autodiscover_tasks(['foo'], force=True)
from celery import Celery
from celery.schedules import crontab

app = Celery('tasks', broker='amqp://127.0.0.1:5672', backend='redis://127.0.0.1:6379/0')

# @app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     # Calls test('hello') every 10 seconds.
#     sender.add_periodic_task(10.0, reverse.s('hello'), name='add every 10')

#     # Calls test('world') every 30 seconds
#     sender.add_periodic_task(30.0, reverse.s('world'), expires=10)

#     # Executes every Monday morning at 7:30 a.m.
#     sender.add_periodic_task(
#         crontab(hour=7, minute=30, day_of_week=1),
#         reverse.s('Happy Mondays!'),
#     )

app.conf.beat_schedule = {
    'add-every-1-minute': {
        'task': 'app.reverse',
        'schedule': crontab(minute='*/1'),
        'args': ('Ahmed',)
    },
}
    
@app.task
def reverse(text):
    return text[::-1]

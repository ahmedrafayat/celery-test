## Broker settings.
broker_url = 'amqp://127.0.0.1:5672'

# List of modules to import when the Celery worker starts.
imports = ('foo.tasks')

## Using the database to store task state and results.
result_backend = 'redis://127.0.0.1:6379/0'

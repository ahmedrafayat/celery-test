from app import app

@app.task
def add(a, b):
    return a + b
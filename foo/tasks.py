from app import app

@app.task
def reverse(text):
    return text[::-1]

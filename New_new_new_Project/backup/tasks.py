from celery import Celery 
from time import sleep
app = Celery('tasks', broker='amqp://cqjouzla:ZXdWkGjatNhWVZC-KbAXvCeeOMdiHTHp@jaguar.rmq.cloudamqp.com/cqjouzla', backend='db+sqlite:///db.sqlite3')

@app.task 
def reverse(text):
    sleep(3)
    return text[::-1]

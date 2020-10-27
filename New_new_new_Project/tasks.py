from celery import Celery 
from time import sleep
import main
import data.inn

app = Celery('tasks')
app.conf.broker_url = 'redis://localhost:6379/0'
app.conf.result_backend = 'redis://localhost:6379/0'

app.conf.broker_transport_options = { 'master_name': "cluster1" }
@app.task 
def myparser(document_type, text):
    sleep(5)
    res = main.Main(document_type, text)  
    return res

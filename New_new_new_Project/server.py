from bottle import route, request, run, template
import tasks
import requests
import json
from time import sleep

document_type = None
text = None

@route('/')
def index():
    global document_type
    global text
    document_type = request.query.document_type or document_type
    text = request.query.text or text
    res = tasks.myparser.delay(document_type, text)
    while res.ready() != True:
        sleep(5)
    res1 = res.get(timeout=7)
    res = json.dumps(res1)
    return res.encode('utf-8').decode('unicode-escape')
    

run(host='127.0.0.1', port=80)
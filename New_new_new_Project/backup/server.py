from bottle import route, request, run, template
import main 
import requests
import json

queue = []

document_type = None
text = None

@route('/input')
def index():
    global document_type
    global text
    document_type = request.query.document_type or document_type
    text = request.query.text or text
    res = main.Main(document_type, text)
    res = json.dumps(res)
    res = res.encode('utf-8').decode('unicode-escape')
    return res
    

run(host='127.0.0.1', port=80)

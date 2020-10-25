import requests

payload = {'document_type': 'coast', 'text':'ИНН 24435535644'}
r = requests.get('http://127.0.0.1/', params=payload)


r = requests.get('http://127.0.0.1/')
print(r.text)


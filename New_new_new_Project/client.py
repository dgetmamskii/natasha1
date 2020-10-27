import requests

payload = {'document_type': 'coast', 'text':'ИНН 24435535644 от 21.12.1999'}
r = requests.get('http://127.0.0.1/', params=payload)

print(r.text)


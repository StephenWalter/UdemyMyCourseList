import requests

r = requests.get('https://google.com')

# test to see if requests is working ok
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
print(r.text)

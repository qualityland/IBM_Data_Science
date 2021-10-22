import requests
url = 'https://www.ibm.com'
r = requests.get(url)
print('status code:', r.status_code)
print('request headers:')
print('================')
for (k, v) in r.request.headers.items():
    print(k + ':', v)
print('response headers:')
print('=================')
for (k, v) in r.headers.items():
    print(k + ':', v)

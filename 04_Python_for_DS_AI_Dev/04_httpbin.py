import requests

# GET
url_get = 'http://httpbin.org/get'
payload = {'name' : 'Joseph', 'ID': '123'}

r = requests.get(url_get, params=payload)
print('GET url:', r.url)
print('request.body:', r.request.body)
print('status_code:', r.status_code)
#print('request as text:\n', r.text)
print('Content-Type:', r.headers['Content-Type'])

# POST
url_post = 'http://httpbin.org/post'
payload = {'name' : 'Joseph', 'ID': '123'}

r_post = requests.post(url_post, data=payload)
print('POST url:', r_post.url)
print('request.body:', r_post.request.body)

# Exercise 

1. Make a request to https://api.agify.io?name=mike but use your name.

```python
import requests
resp = requests.get("https://api.agify.io?name=michael")
data = resp.json()
print(data["age"], data["count"])
```


2. Instead of directly adding your name to the query, pass parameters.

```python
import requests
resp = requests.get("https://api.agify.io?", params={'name': 'Mike'})
data = resp.json()
print(data["age"], data["count"])
```

3. Grab a url, and print the status code and header of the response.  Then print the `Content-Type` of the response (which is in the header)

```python
import requests
resp = requests.get("https://api.agify.io?", params={'name': 'Mike'})
print(resp.status_code)
print(resp.headers)
print(resp.headers['Content-Type'])
```

4. Visit a URL (like https://httpbin.org/status/404) and raise an exception if the status isn’t 200.  You can use  `response.raise_for_status()` to raise the error.  If you don't, the program will continue even though the request failed.  You could also manually raise the exception.


```python
import requests
from requests.exceptions import HTTPError
try:
    resp = requests.get("https://httpbin.org/status/404")
    print(f'The status code was {resp.status_code}')
    resp.raise_for_status() # Raises HTTPError
except HTTPError:
    print('the call failed!')

```

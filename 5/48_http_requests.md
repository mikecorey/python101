# Python requests

## Overview
Python requests is a library that allows you to make web requests to other web services.  These requests can be anything from pulling HTML web pages to (more likely) getting and posting JSON data.

HTTP has become the standard by which information is exchanged on the internet.  Every major company which does business on the internet has an API which allows you to receive information or update their data programmatically.

## Install
Python `requests` has become the standard for making web calls.  It's not part of standard python but can be installed with `pip install`.

> Note there are built in libraries like `urllib` which allow you to make http requests without installing an external package.  However, `requests` has become the preferred library in industry.

```bash
pip install requests
```

Failing to do this pip install step will result in a ModuleNotFoundError being raised.  Again, in a Notebook, we'll use `!pip install requests` with the bang in front.

Then within your script or subsequent code block...

```python
import requests
```

## A Note on Virtual Environments
### Why Virtual Environments
If we're running a python script locally (i.e. not in a Notebook). It's preferred (and in some cases mandated) to install any libraries that we'll use in a virtual environment.  Virtual environments give us the ability to install all our programs external requirements (like `requests`) in an environment specific to the python script we're running.

This is greatly helpful as we avoid requriements conflicts (one library needing v4.0 and another requiring v3.0 for example)  while also letting the developer provide a simple list of all the external libraries that must be installed for this script to execute correctly.

For example if a developer wanted to package their library to a file to be installed by a user, they simply run `pip freeze` which will list a snapshot of their environment.  (Normally this output is sent to `requirements.txt`). The user wishing to run the script can then easily install all prerequisite libraries with `pip install -r requirements.txt`

### Building a Virtual Envionment
`venv` is a very lightweight module for building virtual environments.  This allows us to install a specific python executable and package destination for our entire project.  To set up a virtual environment we call

```bash
python -m venv .venv
source .venv/bin/activate
```

This runs the module `venv` in python which contains the virtual environment creation scripts.  `.venv` is the destination of our virtual environment.  While we could put our venv anywhere in the filesystem, it's good practice to put it in a hidden folder called `.venv` off the root of our project.  This creates a consistent path for finding and activating relevant virtual environments

The second command `source .venv/bin/activate` tells our operating system to run apply the script `activate` to our terminal.  This will change our path to python and point modules to a directory within `.venv` creating this lightweight virtual environment.  When done, we just run `deactivate` (which was also added to our path during `source`)


## HTTP and `GET`
Our simple workflow for getting the contents of a webpage or pinging a http api is as follows:

1. Make the call
    ```python
    resp = requests.get("https://api.github.com/repos/pallets/flask")
    ```

    - `requests.get` simply takes a url as input and returns a response object.

2. Inspect the response
    ```python
    resp.status_code          # 200? 404? 500?
    resp.headers["Content-Type"]
    data = resp.json()        # Convenience shortcut for JSON
    print(data["license"]["name"])
    ```

    The response contains:
        - A status code which is an RFC standard telling us how the request went.  Responses are of types:
        - 1xx: Informational The request was received. (Uncommon but 100 client continue, 101 switch protocols to websockets)
        - 2xx: Success The request was successful (200 ok, 201 created, 204 no content)
        - 3xx: Redirects The request needs to be redirected (301 moved permanently, 304 not modified)
        - 4xx: client error (your fault) (400 bad request, 401 unauthorized (auth failed), 403 forbidden (auth recognized but still no), 404 Not found, 429 Too many requests)
        - 5xx: server error (my fault) (500 Internal Server failure (the server code crashed), 502 bad gateway something upstream or inbetween broke, 503 service unavailable (maintenance), 504 timeout (server churned too long))

    Servers also respond with Headers.  Headers tell us information about the body we're about to receive.  A common one in this case is `Content-Type` which tells us what the body's format will be `text/plain`, `application/json` etc.

    `data` is set to the reponses's body.  in this case we're assuming the response is json (we'll get a ValueError is not.  We can also get .text for the full response as text.)

## Query Parameters and Headers
```python
payload = {"q": "python requests", "sort": "stars"}
hdrs    = {"User-Agent": "Mozilla/5.0"}

resp = requests.get("https://api.github.com/search/repositories",
                    params=payload, headers=hdrs, timeout=10)
```
*`params` is URL‑encoded automatically → `...?q=python+requests&sort=stars`*


## `POST` and other Verbs

| Verb   | Method               | Common Use         | Sample                                               |
|--------|----------------------|--------------------|------------------------------------------------------|
| POST   | `requests.post`      | create / submit forms | ```python
requests.post(url, json=payload)
``` |
| PUT    | `requests.put`       | **replace** a resource | ```python
requests.put(url, data=b"...")
``` |
| PATCH  | `requests.patch`     | **partial** update | ```python
requests.patch(url, json={"name":"new"})
``` |
| DELETE | `requests.delete`    | remove resource    | ```python
requests.delete(url)
``` |

Sending JSON:
```python
payload = {"name": "Ada", "role": "admin"}
resp = requests.post("https://httpbin.org/post", json=payload)
```
`json=` sets header `Content-Type: application/json` for you.

## Sessions, Cookies & Auth
```python
with requests.Session() as s:
    s.headers.update({"Authorization": "Bearer ABC123"})
    s.get("https://api.example.com/me")   # auth header auto‑sent
    s.post("https://api.example.com/logout")
```

### Why use `Session`?

- Reuses TCP connections ⇒ faster  
- Keeps cookies between calls  
- Lets you set default headers / auth once*



## Timeouts
```python
from requests.exceptions import HTTPError, Timeout

try:
    resp = requests.get("https://example.com/slow", timeout=5)
    resp.raise_for_status()          # raises for 4xx/5xx
except Timeout:
    print("Request took too long!")
except HTTPError as e:
    print(f"Bad status: {e.response.status_code}")
```


## File Uploads & Downloads
We can simply send a file in our request using the files parameter in our HTTP request.

```python
# Upload
files = {"file": open("logo.png", "rb")}
requests.post("https://httpbin.org/post", files=files)
```

To Download a file...

```python
# Download large file in chunks
r = requests.get(url, stream=True)
with open("100MB.bin", "wb") as f:
    for chunk in r.iter_content(chunk_size=8192):
        f.write(chunk)
r.close()
```

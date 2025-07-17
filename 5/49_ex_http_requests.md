# Exercise 

1. Make a request to https://api.agify.io?name=mike but use your name.


2. Instead of directly adding your name to the query, pass parameters.


3. Grab a url, and print the status code and header of the response.  Then print the `Content-Type` of the response (which is in the header)


4. Visit a URL (like https://httpbin.org/status/404) and raise an exception if the status isn’t 200.  You can use  `response.raise_for_status()` to raise the error.  If you don't, the program will continue even though the request failed.  You could also manually raise the exception.



# Python network

+ Getting all headers
```python
import urllib.request
req = urllib.request.Request(my_url)
with urllib.request.urlopen(req) as response:
    headers = response.getheaders()
```

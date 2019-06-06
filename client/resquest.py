import urllib.request
content = urllib.request.urlopen("http://localhost:8080").read()
print(content)

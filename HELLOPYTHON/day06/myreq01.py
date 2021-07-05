import requests
URL = 'http://localhost:8090/HELLO/hello.jsp' 
response = requests.get(URL)

print(response.status_code)
print(response.text)

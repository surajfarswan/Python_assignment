import requests
response=requests.get("https://api.forismatic.com/api/1.0/?\
method=getQuote&lang=en&format=jsonp&jsonp=?")
print(response.status_code)
print(response.content)


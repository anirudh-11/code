from urllib2 import Request, urlopen

values = """
  {
    "text": "...your...text...",
    "level": "sentence",
    "bias": {
      "positive": 3.5,
      "neutral": 2.7,
      "negative": 18
    }
  }
"""

headers = {
  'Content-Type': 'application/json; charset=UTF-8'
}
request = Request('https://api.theysay.io/v1/sentiment', data=values, headers=headers)

response_body = urlopen(request).read()
print (response_body)

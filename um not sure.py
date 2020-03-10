from urllib.request import urlopen
import json

link = 'https://quotesondesign.com/wp-json/wp/v2/posts/?orderby=rand'

response = urlopen(link)

data = json.loads(response.read())

print(data)

import requests

#https://newsapi.org/
api_key = 'c05088c3976e4ffd856d9f53960d5e9a'

url = 'https://newsapi.org/v2/everything?q=tesla&from=2024-11-18&' \
      'sortBy=publishedAt&apiKey=' \
      'c05088c3976e4ffd856d9f53960d5e9a'


#make request to the website
request = requests.get(url)

#store the response in a variable
content = request.json()

#access the articles title and description
articles = content['articles']  #access the articles
for article in articles:
    print(article['title'])
    print(article['description'])
    print('---------------------------------')
    


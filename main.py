import requests

url='https://newsapi.org/v2/everything?q=tesla&from=2022-12-19&sortBy=publishedAt&apiKey=94f415fe5e694f04a9fb7ae9e036810e'
apiKEY='94f415fe5e694f04a9fb7ae9e036810e'

response= requests.get(url=url)
print(response.raise_for_status())

content=response.json()
content=content['articles']

def format_article(article):
    formatted_article = f'''
    Author: {article['author']}
    Title: {article['title']}
    Description: {article['description']}
    Link of the article: {article['url']}\n
    '''
    return formatted_article

for article in content:
    art=format_article(article)
    print(art)

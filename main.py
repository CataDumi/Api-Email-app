import requests
from send_email import send_email

url='https://newsapi.org/v2/everything?' \
    'q=tesla&from=2022-12-19&' \
    'sortBy=publishedAt&' \
    'apiKey=94f415fe5e694f04a9fb7ae9e036810e&' \
    'language=en'
apiKEY='94f415fe5e694f04a9fb7ae9e036810e'

header={
    'apiKey':'94f415fe5e694f04a9fb7ae9e036810e',
    'q':'tesla',
    'from':'2023-01-18',
    'language':'en',
    'sortBy':'popularity'

}


response= requests.get(url=url)
print(response.raise_for_status())
content=response.json()
content=content['articles']

def format_article(article):
    formatted_article = f'''
    Author: {str(article['author'])}
    Title: {str(article['title'])}
    Description: {str(article['description'])}
    Link of the article: {str(article['url'])}


    '''
    return formatted_article

txt=''
for article in content[:20]: # asa limitezi sa primesti doar primele 20 de iteme din lista
    art=format_article(article)
    txt+=art

txt = txt.encode('utf-8')
send_email(message=txt)



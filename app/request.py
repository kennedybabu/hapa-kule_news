from app import app
import urllib.request,json
from .models import news

News = news.News

#getting api key
api_key = app.config['NEWS_API_KEY']

#getting the news base url
base_url = app.config['NEWS_API_BASE_URL']


def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category, api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response["articles"]:
            news_results_list = get_news_response["articles"]
            news_results = process_results(news_results_list)

    return news_results

def process_results(news_list):
    '''
    Function that processes the results into the object with the required properties
    
    Args:
        news_list: This is a result after getting the response
        
    Returns:
        A list of objects that only has the required properties
    '''

    news_results_list = []

    for news_item in news_list:
        title = news_item['title']
        description = news_item['description']
        image = news_item['urlToImage']
        author = news_item['author']
        date_created = news_item['publishedAt']
        link = news_item['url']

        if image:
            print(image)
            news_object = News(title, description, image, author, date_created, link)
            news_results_list.append(news_object)
    
    return news_results_list

def get_news_item(id):
    get_news_details_url = base_url.format(id, api_key)

    with urllib.request.urlopen(get_news_details_url)as url:
        news_details_data = url.read()
        news_details_response = json.loads(news_details_data)

        news_object = None

        if news_details_response:
            title = news_details_response.get('title')
            description = news_details_response.get('description')
            image = news_details_response.get('urlToImage')
            author = news_details_response.get('author')
            date_created = news_details_response.get('publishedAt')
            link = news_details_response.get('url')

            news_object = News(title, description, image, author, date_created, link)

    return news_object

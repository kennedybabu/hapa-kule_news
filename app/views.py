from flask import render_template
from app import app
from .request import get_news
from datetime import date, datetime

@app.route('/')
def index():
    '''
    view root page function that returns the index page and its data
    '''
    today = date.today()
    current_date = today.strftime("%B %d, %Y")
    #getting general news
    general_news = get_news('general')
    title = "Hapa Kule News - Home of your news needs"
    return render_template('index.html', title = title, general = general_news, current_date = current_date)

@app.route('/news/<int:news_id>')
def news(news_id):
    '''
    View news page function that returns the  news details page and its data
    '''
    
    title = "Hapa Kule News - Home of your news needs"
    return render_template('news.html', id = news_id, title = title)

@app.route('/sports')
def sports():
    '''
    Function that will return news in the sports category
    '''
    sports_news = get_news('sports')
    return render_template('sports.html', sports = sports_news)

@app.route('/business')
def business():
    '''
    Function that will return news in the business category
    '''
    business_news = get_news('business')
    return render_template('business.html', business = business_news)
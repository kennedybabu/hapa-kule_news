from flask import render_template, request, redirect, url_for
from . import main
from ..request import get_news
from datetime import date, datetime

today = date.today()


@main.route('/')
def index():
    '''
    view root page function that returns the index page and its data
    '''
    current_date = today.strftime("%B %d, %Y")
    #getting general news
    general_news = get_news('general')
    title = "Hapa Kule News - Home of your news needs!"
    return render_template('index.html', title = title, general = general_news, current_date = current_date)

@main.route('/news/<int:news_id>')
def news(news_id):
    '''
    View news page function that returns the  news details page and its data
    '''
    
    title = "Hapa Kule News - Home of your news needs"
    return render_template('news.html', id = news_id, title = title)

@main.route('/sports')
def sports():
    '''
    Function that will return news in the sports category
    '''
    sports_news = get_news('sports')
    title = "Hapa Kule News - Sports"
    return render_template('sports.html', sports = sports_news, title = title)

@main.route('/business')
def business():
    '''
    Function that will return news in the business category
    '''
    business_news = get_news('business')
    title = "Hapa Kule News - Business"
    return render_template('business.html', business = business_news, title = title)

@main.route('/entertainment')
def entertainment():
    '''
    Function that will return news in the entertainment category
    '''
    entertainment_news = get_news('entertainment')
    title = "Hapa Kule News - Entertainment"

    return render_template('entertainment.html', entertainment = entertainment_news, title = title)

@main.route('/technology')
def science():
    '''
    Function that will return news in the technology category
    '''
    science_news = get_news('science')
    title = "Hapa Kule News - Science"

    return render_template('science.html', science = science_news, title = title)
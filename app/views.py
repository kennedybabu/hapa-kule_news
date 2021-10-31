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
    general_news = get_news('sports')
    title = "Hapa Kule News - Home of your news needs"
    return render_template('index.html', title = title, general = general_news, current_date = current_date)

@app.route('/news/<int:news_id>')
def news(news_id):
    '''
    View news page function that returns the  news details page and its data
    '''
    
    title = "Hapa Kule News - Home of your news needs"
    return render_template('news.html', id = news_id, title = title)
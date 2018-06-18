from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources,get_article



@main.route('/')
def index():
    """
    Function that returns the index page and all its data
    """
    sport_news = get_sources('sports')
    tech_news = get_sources('technology')
    title = 'ZIGS News-Breaking News,Latest News & Headlines'
    return render_template('index.html', title=title, sports=sport_news, technology=tech_news)

#
@main.route('/source/<id>')
def articles(id):
    """
    View articles
    """
    article = get_article(id)
    print(article)
    title = f'ZIGS News ~ {id}'
    return render_template('news.html', title=title, article=article)
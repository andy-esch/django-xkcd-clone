"""Render XKCD like it is on the xkcd.com but with Django
XKCD JSON 'API': https://xkcd.com/json.html
"""
import random

import requests

from django.template import loader
from django.http import HttpResponse

MAX_COMIC_NUM = requests.get('http://xkcd.com/info.0.json').json().get('num', 1998)
COMIC_ENDPOINT = 'http://xkcd.com/{}/info.0.json'

# Create your views here.

def index(request):
    """Return most recent comic"""
    return get_comic(request)

def get_comic(request, num=MAX_COMIC_NUM):
    """Get specific comic. If num is not specified get most recent."""
    if num > MAX_COMIC_NUM:
        num = MAX_COMIC_NUM
    template = loader.get_template('template.html')
    resp = requests.get(COMIC_ENDPOINT.format(num))
    context = xkcdify_response(resp)
    return HttpResponse(
        template.render(context, request)
    )

def xkcdify_response(resp):
    """Turn requests response into template context"""
    context = {
        'rand_num': random.randint(0, MAX_COMIC_NUM),
        'comic_prev': resp.json()['num'] - 1,
        'next_num': resp.json()['num'] + 1,
        'max_comic': MAX_COMIC_NUM,
        'comic_num': resp.json()['num'],
        'title': resp.json()['safe_title'],
        'alt': resp.json()['alt'],
        'img': resp.json()['img'],
    }
    return context

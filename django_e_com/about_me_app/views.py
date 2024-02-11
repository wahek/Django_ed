import functools

from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.debug(f'func:{func.__name__}')
        return result

    return wrapper


html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>About_me</title>
</head>
<body>
    <header>
        <h1>Привет, это учебный проект на Django</h1>
        <h2>Поехали</h2>
    </header>
</body>
</html>'''


@log
def index(request):
    return render(request, 'index.html')


@log
def about(request):
    return HttpResponse(html)

from django.http import HttpResponse
from django.shortcuts import render
from urllib.request import urlopen

from bs4 import BeautifulSoup
from bs4.element import Comment
from .forms import InputForm
from .forms import DateForm
from .strings_counter import RedisClient
from .strings_counter import StringsCounter

def index(request):
    dic = None
    text = ""
    redis = RedisClient()
    r = {}
    date = ""

    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            input_received = form.cleaned_data['input']
            date = form.cleaned_data['date']
            link = input_received
            try:
                html = urlopen(link)
            except Exception:
                return render(request, 'verificacion/error.html')
            soup = BeautifulSoup(html, 'html.parser')

            for tag in soup.findAll('p'):
                text += " " + str(tag.get_text())

            sc = StringsCounter()
            dic = sc.count_strings(text)
            redis.save_dic(date, dic)
            r = redis.imprimir_dic(date)
            # for keys in r:
                # print(str(keys).replace("b'", "").replace("'", ""), str(r[keys]).replace("b'", "").replace("'", ""))

    context = {
        'palabras': dic,
        'fecha' : date,
        'form': InputForm()
    }
    return render(request, 'verificacion/index.html', context)


def test(request):
    return render(request, 'verificacion/test.html')

def history(request):
    redis = RedisClient()
    r = {}
    if request.method == 'POST':
        form = DateForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            r = redis.imprimir_dic(date)

    context = {
        'form': DateForm(),
        'palabras': redis.normalize_data(r)
    }
    return render(request, 'verificacion/history.html', context)
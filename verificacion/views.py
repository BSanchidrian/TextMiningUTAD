from django.http import HttpResponse
from django.shortcuts import render
from urllib.request import urlopen
from bs4 import BeautifulSoup
from bs4.element import Comment 
from .forms import InputForm
from .strings_counter import StringsCounter

def tag_visible(element):
    if element.parent.name in ['p', 'a', 'span']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts) 
    return u" ".join(t.strip() for t in visible_texts)

def index(request):
    dic = None
    text = ""

    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            input_received = form.cleaned_data['input']
            date = form.cleaned_data['date']
            print(date)
            link = input_received
            html = urlopen(link)
            soup = BeautifulSoup(html,'html.parser')

            for tag in soup.findAll('p'):
                text += " " + str(tag.get_text())

            sc = StringsCounter()
            dic = sc.count_strings(text)

    context = {
        'palabras': dic,
        'form': InputForm()
    }
    return render(request, 'verificacion/index.html', context)

from django.http import HttpResponse
from django.shortcuts import render
import urllib.request

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):

    def init(self):
        self.text = ""

    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print("Encountered some data  :", data)
        self.text += str(data)
        self.text += " "

from .forms import InputForm
from .strings_counter import StringsCounter

def index(request):
    dic = None
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            input_received = form.cleaned_data['input']
            print(type(input_received))

            link = input_received
            f = urllib.request.urlopen(link)
            text = f.read()
            parser = MyHTMLParser()
            parser.init()
            parser.feed(str(text))

            sc = StringsCounter()
            dic = sc.count_strings(parser.text)
            # print(dic)

    context = {
        'palabras': dic,
        'form': InputForm()
    }
    return render(request, 'verificacion/index.html', context)

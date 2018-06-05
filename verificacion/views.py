from django.http import HttpResponse
from django.shortcuts import render
import urllib.request

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
            print(text)

            # sc = StringsCounter()
            # dic = sc.count_strings(input_received)
            # print(dic)

    context = {
        'palabras': dic,
        'form': InputForm()
    }
    return render(request, 'verificacion/index.html', context)

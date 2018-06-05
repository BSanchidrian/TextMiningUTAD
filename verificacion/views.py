from django.http import HttpResponse
from django.shortcuts import render

from .forms import InputForm
from .strings_counter import StringsCounter

def index(request):
    dic = None
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            # TODO
            input_received = form.cleaned_data['input']
            print(type(input_received))
            sc = StringsCounter()
            dic = sc.count_strings(input_received)
            print(dic)

    context = {
        'palabras': dic,
        'form': InputForm()
    }
    return render(request, 'verificacion/index.html', context)

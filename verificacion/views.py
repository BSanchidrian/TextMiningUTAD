from django.http import HttpResponse
from django.shortcuts import render
import feedparser

from .forms import InputForm
from .strings_counter import StringsCounter

def index(request):
    text = ""
    link = "http://ep00.epimg.net/rss/elpais/portada.xml"
    feed = feedparser.parse(link)
    print(feed["channel"]["title"])

    for item in feed["items"]:
        text += item["title"]
        text += " "
        text += item["description"] 
        # text += item["content:encoded"]
        try:
            text += " "
            text += item.content        
        except Exception:
            pass
        # print(item["title"])
        # print(item["description"])
        # print("\n\n")


    sc = StringsCounter()
    dic = sc.count_strings(text)
    # print(dic)

    context = {
        'palabras': dic
    }
    return render(request, 'verificacion/index.html', context)

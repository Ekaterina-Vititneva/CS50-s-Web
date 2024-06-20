from django.shortcuts import render
from django.http import Http404

from . import util

from markdown2 import Markdown


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
    
def title(request, title):
    markdowner = Markdown()
    try:
        content = markdowner.convert(util.get_entry(title))
    except:
        raise Http404("Title does not exist")
    return render(request, "encyclopedia/title.html", {
        "title": title,
        "title_content": content
    })
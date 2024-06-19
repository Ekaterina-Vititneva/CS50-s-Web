from django.shortcuts import render

from . import util

from markdown2 import Markdown


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
    
def title(request, title):
    markdowner = Markdown()
    return render(request, "encyclopedia/title.html", {
        "title": title,
        "title_content": markdowner.convert(util.get_entry(title))
    })
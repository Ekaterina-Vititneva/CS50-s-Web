from django.shortcuts import render, redirect
from django.http import Http404

from . import util

from markdown2 import Markdown
from random import randint, choice


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
    
def title(request, title):
    #print(title)
    markdowner = Markdown()
    try:
        content = markdowner.convert(util.get_entry(title))
    except:
        raise Http404("Title does not exist")
    return render(request, "encyclopedia/title.html", {
        "title": title,
        "title_content": content
    })
    
def search(request, query):
    all_entries = util.list_entries()
    if query in all_entries:
        return redirect('title_1', title=query)

def random(request):
    all_entries = util.list_entries()
    if not all_entries:
        raise Http404("No entries available")
    random_entry = choice(all_entries)
    return redirect('title_1', title=random_entry)
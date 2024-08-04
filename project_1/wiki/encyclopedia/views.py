from django.shortcuts import render, redirect
from django.http import Http404

from . import util

from markdown2 import Markdown
from random import randint, choice

import os


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

def search(request):
    query = request.GET.get('q')
    if not query:
        return redirect('index')

    entries = util.list_entries() 
    entries_lower = [entry.lower() for entry in entries]
    if query.lower() in entries_lower:
        return redirect('title_1', title=query)
    results = [entry for entry in entries if query.lower() in entry.lower()]
    return render(request, "encyclopedia/search.html", {
        "query": query,
        "results": results
    })     

def random(request):
    all_entries = util.list_entries()
    if not all_entries:
        raise Http404("No entries available")
    random_entry = choice(all_entries)
    return redirect('title_1', title=random_entry)

def create(request):
    return render(request, "encyclopedia/create.html")
    
def save(request):
    new_title = request.POST.get('new-title')
    content = request.POST.get('content')
    all_entries = util.list_entries()
    if new_title not in all_entries:
        entries_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'entries')
        file_path = os.path.join(entries_dir, f"{new_title}.md")
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(f"# {new_title}\n\n{content}")
        return redirect('title_1', title=new_title)
    else:
        raise Http404("Another encyclopedia entry already exists with the provided title")
    
def edit(request):
    pass
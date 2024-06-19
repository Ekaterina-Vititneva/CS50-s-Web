from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
    
def title(request):
    title = "CSS"
    return render(request, "encyclopedia/title.html", {
        "title": title,
        "title_content": util.get_entry(title)
    })


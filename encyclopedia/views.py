from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

# step 1 : entry page function

def entry_page(request, title):
    content = util.get_entry(title)
    print(f"Title: {title}, Content: {content}") 
    if content == None:
        return render(request, 'encyclopedia/error.html', {'message':'Page not Found!'})
    return render(request, 'encyclopedia/entry.html', {
        'title': title,
        'content': content,    
    })
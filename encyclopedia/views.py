from django.shortcuts import render
import markdown2
from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

# step 1 : entry page function

def entry_page(request, title):
    entries = util.list_entries()
    for entry in entries:
        # print entry on  console
        print(f"Checking entry: {entry}")
        if entry.lower() == title.lower():
            title = entry
            content = util.get_entry(title)
            content = markdown2.markdown(content)
            # print title and content on console
            print(f"Title: {title}, Content: {content}") 
            return render(request, 'encyclopedia/entry.html', {
                'title': title,
                'content': content,    
            })
        
    return render(request, 'encyclopedia/error.html', {'message':'Page not Found!'})
    
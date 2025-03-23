from django.shortcuts import render, redirect
import markdown2
from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

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
    
def search(request):
    # check if function is working
    print(f"search function triggered")
    entries = util.list_entries()
    query = request.GET.get('q', '').strip()
    queryArray = []
    
    # print query on console
    print(f"search query: {query}")
    
    for entry in entries:
        # check entry
        print(f"checking entry: {entry}")
        
        if query.lower() == entry.lower():
            content = util.get_entry(entry)
            # print content of entry
            print(f"content of entry: {content}")
            return render(request, 'encyclopedia/entry.html', {
                'title': entry,
                'content': markdown2.markdown(content),    
            })
            
        elif query.lower() in entry.lower():
            queryArray.append(entry)
            
    # print search results for partial matches        
    print(f"search results: {queryArray}")    
        
    return render(request, 'encyclopedia/search.html', {
        'query': query,
        'queryArray': queryArray,    
    })
    
def new_page(request):
    
    
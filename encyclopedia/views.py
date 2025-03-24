from django.shortcuts import render, redirect
from django.urls import reverse
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
        
    return render(request, 'encyclopedia/error.html', {
        'message':'Page not Found!'
    })
    
    
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
    
    # print request method
    print(f"Request Method: {request.method}") 
    
    if request.method == 'POST':
        # check if request is received
        print("POST request received!")
        title = request.POST.get('title', '').strip()
        content = request.POST.get('content').strip()

        # print title and content on console
        print(f"Received Title: {title}")
        print(f"Received Content: {content}")
        
        if not title or not content:
            return render(request, 'encyclopedia/error.html', {
                'message' : 'Insufficient Information! Please Try Again.' 
            })
            
        entries = util.list_entries()
        for entry in entries:
            if title.lower() == entry.lower():
                return render(request, 'encyclopedia/error.html', {
                    'message':'This entry already exists!'
                })
        
        util.save_entry(title, content)
        
    return render(request, 'encyclopedia/new_page.html')


def edit_entry(request, title):
    
    # print request method
    print(f"Request Method: {request.method}") 
    
    if request.method == 'POST':
        # check if request is received
        print("POST request received!")
        content = request.POST.get('content').strip()

        # print content on console
        print(f"Received Content: {content}")
        
        if not content:
            return render(request, 'encyclopedia/error.html', {
                'message' : 'Content cannot be empty.' 
            })
        
        util.save_entry(title, content)
        return redirect(reverse('entry', kwargs={'title':title}))
        
    content = util.get_entry(title)
        
    return render(request, 'encyclopedia/edit.html', {
        'title': title,
        'content': content
    })
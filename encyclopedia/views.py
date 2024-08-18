from django.shortcuts import render
import markdown2
from . import util
import random

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entry_names": util.list_entries()
    })

# takes the phrase after 'wiki/' 
    # adds it the top
    # takes the markdown from 'entries' and passes "article" to entry.html

def wiki(request, entry):
    return render(request, "encyclopedia/entry.html", {
        "article": markdown_convert(entry),
    })

def markdown_convert(entry):
    single_entry = entry.capitalize()
    article = util.get_entry(single_entry)
    return markdown2.markdown(article)

def search(request):
    if request.method == 'GET':
        search_term = request.GET.get('q', '')  # Get the 'q' value from the query string, default to empty string if not present
        search_term = search_term.lower()
        filtered_list = [s for s in util.list_entries() if search_term in s.lower()]
    
        context = {
            'search_results': filtered_list,  # Replace 'your_search_results' with the actual results you get
            'search_term': search_term,  # Pass the search term to the template as well
        }
        return render(request, 'encyclopedia/search.html', context)
    else:
        return render(request, 'encyclopedia/search.html')

def random_article(request):
    list_entry = util.list_entries()
    answer = random.choice(list_entry)
    return wiki(request, f'{answer}')
"""  
def add(request):
    return render(request, "encyclopedia/add.html", {
        "form": NewTaskForm()
    }) """
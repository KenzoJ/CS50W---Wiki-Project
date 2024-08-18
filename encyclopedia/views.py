from django.shortcuts import render
import markdown2
from . import util

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



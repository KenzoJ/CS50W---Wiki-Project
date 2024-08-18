from django.shortcuts import render
import markdown2
from . import util
import random
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect


def index(request):
    if "tasks" not in request.session:

        # If not, create a new list
        request.session["tasks"] = []

    return render(request, "encyclopedia/index.html", {
        "tasks": request.session["tasks"]
    })
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

def add(request):
    if request.method == "POST":

        # Take in the data the user submitted and save it as form
        form = NewTaskForm(request.POST)

        # Check if form data is valid (server-side)
        if form.is_valid():

            # Isolate the task from the 'cleaned' version of form data
            task = form.cleaned_data["task"]

            # Add the new task to our list of tasks
            tasks.append(task)

            # Redirect user to list of tasks
            return HttpResponseRedirect(reverse("index"))

        else:

            # If the form is invalid, re-render the page with existing information.
            return render(request, "tasks/add.html", {
                "form": form
            })

    return render(request, "encyclopedia/add.html", {
        "form": NewTaskForm()
    })


class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")

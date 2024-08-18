from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki", views.index, name='wiki'),
    path("wiki/<str:entry>", views.wiki, name='article'),
    path("search/", views.search, name='search_results'),
    path("random", views.random_article, name='random_article'),
    path("add", views.add, name="add")
]

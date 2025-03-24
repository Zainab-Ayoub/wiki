from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('wiki/search/', views.search, name='search'),
    path("wiki/new_page/", views.new_page, name='new_page'),
    path("wiki/<str:title>/", views.entry_page, name="entry"),
    path("wiki/<str:title>/edit/", views.edit_entry, name="edit_page"),
    path("wiki.<str:title>/random/", views.random_page, name='random_page')
]

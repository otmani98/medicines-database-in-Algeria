from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("search",views.SearchView.as_view(), name="search"),
    path("all",views.lista, name="all"),
    path("all/<order>",views.orderfunc, name="ordered"),
]

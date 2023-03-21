from django.shortcuts import render
from django.views import View
from .models import MedicinesModel
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, Http404


class IndexView(View) :
    #this class for rendering index page
    #and I use it to delete sessions that belongs to searching.

    def get(self, request):

            request.session["idis"] = []
            request.session["empty_value"] = False
            request.session["after_search"] = False

            return render(request, "main_app/index.html")

class SearchView(View) :
        #here I used the sessions to save the result because of paginator,
        #it delete the result when click any button that belongs to it.

        def get(self, request):
        #this function shows the result of searching by accsessing to sessions
        #and take the group of id that belong to result and makes the query by them

            after_search = request.session.get("after_search")
            empty_value = request.session.get("empty_value")
            idis = request.session.get("idis")
            search_value = request.session.get("search_value")

            paginator = Paginator(MedicinesModel.objects.filter(id__in=idis).order_by("bn"), 21)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)

            return render(request, "main_app/index.html", {
                "after_search" : after_search,
                "empty_value" : empty_value,
                "page_obj" : page_obj,
                "search_value" : search_value
            })


        def post(self, request):
        #this function saves the result of searching as group of id in session
        #and redirects to page of searching to get method

            search_value = request.POST["search-input"]

            if search_value:
                results = MedicinesModel.objects.filter(Q(inn__icontains=search_value) | Q(bn__icontains=search_value) | Q(form__icontains=search_value)| Q(laboratories__icontains=search_value)| Q(country__icontains=search_value)| Q(dosing__icontains=search_value))
                request.session["search_value"] = search_value
                request.session["empty_value"] = False

            else:
                request.session["idis"] = []
                request.session["empty_value"] = True
                request.session["after_search"] = False
                request.session["search_value"] = ""
                return HttpResponseRedirect("search")

            stored_list = []

            if results:
                for result in results:
                    stored_list.append(result.id)
                
            request.session["idis"] = stored_list
            request.session["after_search"] = True

            return HttpResponseRedirect("search")


def lista(request):
    # this function shows all medecines

    medicines_list = MedicinesModel.objects.all()

    paginator = Paginator(medicines_list, 21) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'main_app/all.html', {'page_obj': page_obj})


def orderfunc(request, order):
    # this function orders the all medecines by many fields.

    if order in ("bn", "inn", "form", "laboratories", "country") :

        medicines_list = MedicinesModel.objects.order_by(order)
        paginator = Paginator(medicines_list, 21) 
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, 'main_app/all.html', {'page_obj': page_obj})

    else:
        raise Http404()
    
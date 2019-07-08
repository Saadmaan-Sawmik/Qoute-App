from django.shortcuts import render
from django.views.generic import ListView

from .models import QouteCategory, Qoute


class HomeView(ListView):

    model               = Qoute             # same as queryset = Qoute.objects.all()
    paginate_by         = 2                 # I set it by 2 so that you can see my pagination setup easyly
    template_name       = 'home.html'
    context_object_name = 'qoute_list'


    def get_queryset(self, **kwarg):
        query_set = super().get_queryset(**kwarg)
        return query_set.select_related('qoute_category')







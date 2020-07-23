from django.shortcuts import render, redirect
from operator import attrgetter
from django.http import HttpResponse, HttpResponseNotFound


from django.views.generic import DetailView, ListView, View


from blog.models import BlogPost


class homey(ListView):

    def get_queryset(self, *args, **kwargs):

        qs = BlogPost.objects.all()
        print(self.request.GET)
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(title__icontains=query)

        return qs

    model = BlogPost
    paginate_by = 7
    template_name = 'personal/home.html'

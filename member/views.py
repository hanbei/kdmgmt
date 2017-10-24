from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic

# Create your views here.
from .models import Member


class ListView(generic.ListView):
    template_name = 'member/member_list.html'
    context_object_name = 'members'

    def get_queryset(self):
        return Member.objects.order_by('name')


class DetailView(generic.DetailView):
    model = Member
    template_name = 'member/member_detail.html'

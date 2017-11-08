from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.urls import reverse, reverse_lazy
from django.views import generic

# Create your views here.
from .models import Member, Group


def export_group_to_csv(request, group_id):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="kader.csv"'

    # The data is hard-coded here, but you could load it from a database or
    # some other source.
    group = Group.objects.get(pk=group_id)
    csv_data = group.member_set.all().order_by('name')

    t = loader.get_template('member/csv.txt')
    c = {
        'data': csv_data,
    }
    response.write(t.render(c))
    return response


def do_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('member:group_index'))
        else:
            return redirect(reverse('member:login'))
    else:
        return render(request, 'member/login.html')


def do_logout(request):
    logout(request)
    return redirect(reverse('member:login'))


class MemberListView(LoginRequiredMixin, generic.ListView):
    template_name = 'member/member_list.html'
    context_object_name = 'members'
    login_url = reverse_lazy('member:login')

    def get_queryset(self):
        return Member.objects.order_by('name')


class MemberDetailView(LoginRequiredMixin, generic.DetailView):
    model = Member
    template_name = 'member/member_detail.html'
    login_url = reverse_lazy('member:group_index')


class GroupListView(LoginRequiredMixin, generic.ListView):
    template_name = 'group/list.html'
    context_object_name = 'groups'
    login_url = reverse_lazy('member:login')

    def get_queryset(self):
        return Group.objects.order_by('name')

class GroupDetailView(LoginRequiredMixin, generic.DetailView):
    model = Group
    template_name = 'group/detail.html'
    login_url = reverse_lazy('member:group_index')

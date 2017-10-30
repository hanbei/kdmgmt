from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.urls import reverse, reverse_lazy
from django.views import generic

# Create your views here.
from .models import Member


def export_to_csv(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="kader.csv"'

    # The data is hard-coded here, but you could load it from a database or
    # some other source.
    csv_data = Member.objects.order_by('name')

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
            return redirect(reverse('member:index'))
        else:
            return redirect(reverse('member:login'))
    else:
        return render(request, 'member/login.html')


def do_logout(request):
    logout(request)
    return redirect(reverse('member:login'))


class ListView(LoginRequiredMixin, generic.ListView):
    template_name = 'member/member_list.html'
    context_object_name = 'members'
    login_url = reverse_lazy('member:login')  # '/login/'

    def get_queryset(self):
        return Member.objects.order_by('name')


class DetailView(LoginRequiredMixin, generic.DetailView):
    model = Member
    template_name = 'member/member_detail.html'
    login_url = reverse_lazy('member:index')  # '/login/'

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.urls import reverse, reverse_lazy
from django.views import generic

# Create your views here.
from .models import Member, Group


@login_required
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
            return redirect(reverse('member:group_list'))
        else:
            return redirect(reverse('member:login'))
    else:
        return render(request, 'login.html')


def do_logout(request):
    logout(request)
    return redirect(reverse('member:login'))


class MemberListView(LoginRequiredMixin, generic.ListView):
    template_name = 'member/list.html'
    context_object_name = 'members'
    login_url = reverse_lazy('member:login')

    def get_queryset(self):
        return Member.objects.order_by('name')


class MemberDetailView(LoginRequiredMixin, generic.DetailView):
    model = Member
    template_name = 'member/detail.html'
    login_url = reverse_lazy('member:group_list')


@login_required
def group_list_view(request):
    groups = Group.objects.filter(users__id=request.user.id).order_by('name')
    return render(request, 'group/list.html', {'groups': groups})


@login_required
def group_detail_view(request, pk):
    group = get_object_or_404(Group, pk=pk, users__id=request.user.id)
    return render(request, 'group/detail.html', {'group': group})

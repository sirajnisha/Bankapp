from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import User, Branch
from .forms import UserForm
from django.shortcuts import render

class UserListView(ListView):
    model = User
    form_class = UserForm
    context_object_name = 'users'

class UserCreateView(CreateView):
    model =User
    form_class = UserForm
    success_url = reverse_lazy('user_changelist')

class UserUpdateView(UpdateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('user_changelist')

def load_branches(request):
    district_id = request.GET.get('district')
    branches = Branch.objects.filter(district_id=district_id).order_by('name')
    return render(request, 'user/branch_dropdown_list_options.html', {'branches': branches})
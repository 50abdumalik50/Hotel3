from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth import get_user_model
from django.shortcuts import render

from apps.users.forms import UserCreateForm

User = get_user_model()


class UserCreateView(CreateView):
    model = User
    form_class = UserCreateForm
    template_name = 'auth/register.html'
    success_url = reverse_lazy('login')

    # def login_logics(request):
    #     return render(request, 'auth/login.html', locals())

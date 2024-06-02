# from django.urls import reverse_lazy
# from django.views.generic.edit import CreateView
# from django.contrib.auth import get_user_model
# from django.shortcuts import render
#
# from apps.auth.forms import UserCreateForm
#
# User = get_user_model()
#
#
# class UserCreateView(CreateView):
#     model = User
#     form_class = UserCreateForm
#     template_name = 'auth/register.html.html'
#     success_url = reverse_lazy('login')
#
#     def login_logics(request):
#         return render(request, 'auth/login.html', locals())




from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import get_user_model
from django.contrib.auth import login, authenticate, logout
from django.views.decorators.csrf import csrf_protect

from apps.users.forms import UserCreationForm, UserUpdateForm, UserRegisterForm, UserLoginForm
from django.views.generic import DeleteView
from django.contrib.auth.models import User
from django.views import View


User = get_user_model()

class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')

class UserCreateView(generic.CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'auth/account.html'
    success_url = '/index.html'


class UserDetailView(generic.DetailView):
    model = User
    template_name = 'auth/users_detail.html'
    context_object_name = 'user'


class UserUpdateView(generic.UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'auth/users_update.html'
    context_object_name = 'user'
    success_url = '/profile/'


class UserProfileView(generic.DetailView):
    model = User
    template_name = 'auth/user_profile.html'
    context_object_name = 'user'

    def get_object(self, queryset=None):
        return self.request.user

class UserDeleteView(DeleteView):
    model = User
    template_name = 'auth/user_delete.html'
    context_object_name = 'user'
    success_url = '/index.html'


class RegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'auth/register.html', {'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse_lazy('home'))
        return render(request, 'auth/register.html', {'form': form})

class LoginView(View):
    def get(self, request):
        form = UserLoginForm()
        return render(request, 'auth/login.html', {'form': form})

    def post(self, request):
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        return render(request, 'auth/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')






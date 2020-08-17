from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, LoginForm


class Register(SuccessMessageMixin, generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('home')
    template_name = 'register.html'
    success_message = "Your Account was succesfully created "


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)

        if form.is_valid():
            data = form.cleaned_data
            new_user = authenticate(
                request,
                username=data['username'],
                password=data['password'])
            if new_user is not None:
                login(request, new_user)
                messages.success(request, f'Welcome Back! {new_user.username}')
                return redirect('home')
            else:
                messages.error(
                    request, 'User Does Not exist or Invalid Login Credentials')
                return redirect('login')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')
    else:
        form = LoginForm()

        return render(request, 'login.html', {'form': form})

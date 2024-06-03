# profiles/views.py
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            user = authenticate(username=user.username, password=form.cleaned_data['password'])
            login(request, user)
            return redirect('shopapp:home')
    else:
        form = RegisterForm()
    return render(request, 'myaccount/register.html', {'form': form})

class UserLoginView(LoginView):
    template_name = 'myaccount/login.html'


def logout_view(request: HttpRequest):
    logout(request)
    return redirect(reverse("myaccount:login"))





from django.contrib.auth import login, authenticate
from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib.auth.decorators import login_required
# Create your views here.
from Accounts.forms import UserLoginForm


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/dashboard')
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/dashboard')

    context = {
        'form': form,
    }
    return render(request, "login.html", context)
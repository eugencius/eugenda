from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages

from . import forms


# Create your views here.


def register_view(request):
    if request.user.is_authenticated:
        return redirect('contacts:index')

    if request.method == "POST":
        form = forms.RegisterForm(request.POST)

        if form.is_valid():
            password = request.POST.get('password')

            user = form.save(commit=False)
            user.set_password(password)

            user.save()

            messages.add_message(
                request, messages.SUCCESS, "Registered successfully! Now you just have to sign in.")

            return redirect('accounts:login')

    else:
        form = forms.RegisterForm()

    return render(request, 'accounts/register.html', {
        "form": form,
        "exclude_navbar": True,
    })


def login_view(request):
    next_page = request.GET.get('next', 'contacts:index')

    if request.user.is_authenticated:
        return redirect('contacts:index')

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)

            messages.add_message(request, messages.SUCCESS,
                                 "You logged sucessfully!")
            return redirect(next_page)

        else:
            messages.add_message(request, messages.ERROR,
                                 "Your username or password are wrong")

    login_form = forms.LoginForm()

    return render(request, 'accounts/login.html', {
        "form": login_form,
        "exclude_navbar": True,
        "next": next_page,
    })


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.add_message(request, messages.WARNING,
                             "You loggged out.")
        return redirect('accounts:login')

    return redirect('contacts:index')

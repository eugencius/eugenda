from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from django.views.generic import FormView, View
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User

from . import forms


# Create your views here.


class RedirectAuthenticatedUser:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("contacts:index")

        return super().dispatch(request, *args, **kwargs)


class Register(RedirectAuthenticatedUser, CreateView):
    model = User
    form_class = forms.RegisterForm
    template_name = "accounts/register.html"

    def form_valid(self, form):
        password = self.request.POST.get("password")

        user = form.save(commit=False)
        user.set_password(password)

        user.save()

        messages.add_message(
            self.request,
            messages.SUCCESS,
            "Registered successfully! Now you just have to sign in.",
        )

        return redirect("accounts:login")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update({"exclude_navbar": True})

        return context


class Login(RedirectAuthenticatedUser, View):
    form_class = forms.LoginForm
    template_name = "accounts/login.html"

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        self.next_page = self.request.GET.get("next", "contacts:index")

        self.context = {
            "form": self.form_class(),
            "exclude_navbar": True,
            "next": self.next_page,
        }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        username = self.request.POST.get("username")
        password = self.request.POST.get("password")

        user = authenticate(self.request, username=username, password=password)

        if user:
            login(self.request, user)

            messages.add_message(
                self.request, messages.SUCCESS, "You logged sucessfully!"
            )
            return redirect(self.next_page)

        else:
            messages.add_message(
                self.request, messages.ERROR, "Your username or password are wrong"
            )
            return redirect("accounts:login")


def logout_view(request):
    if request.method == "POST":
        logout(request)
        messages.add_message(request, messages.WARNING, "You loggged out.")
        return redirect("accounts:login")

    return redirect("contacts:index")

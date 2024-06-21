from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

from . import forms
from .models import Contact


User = get_user_model()
# Create your views here.


@login_required(login_url="accounts:login")
def index_view(request):
    user = User.objects.get(username=request.user.username)
    contacts = Contact.objects.filter(creator=user)

    return render(
        request,
        "contacts/index.html",
        {
            "contacts": contacts,
        },
    )


@login_required(login_url="accounts:login")
def create_contact(request):
    if request.method == "POST":
        form = forms.CreateContactForm(request.POST)

        if form.is_valid():
            creator = User.objects.get(username=request.user.username)
            contact = form.save(commit=False)
            contact.creator = creator
            contact.image = request.FILES.get("image")

            contact.save()

            messages.add_message(
                request, messages.SUCCESS, "A new contact was created!"
            )

            return redirect("contacts:index")

    else:
        form = forms.CreateContactForm()

    return render(request, "contacts/create_contact.html", {"form": form})

from typing import Any
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from django.db.models import Q

from . import forms
from .models import Contact
from templates.static import utils


User = get_user_model()
LOGIN_URL = "accounts:login"


# Create your views here.


@login_required(login_url=LOGIN_URL)
def index_view(request):
    user = User.objects.get(username=request.user.username)

    per_page = 9
    contacts = Contact.objects.filter(creator=user).order_by("-id")
    paginator = Paginator(contacts, 9)

    current_page = int(request.GET.get("page", 1))
    page_obj = paginator.get_page(current_page)
    page_range = utils.make_pagination(current_page, paginator.page_range, max_pages=6)

    return render(
        request,
        "contacts/index.html",
        {
            "page_range": page_range,
            "page_obj": page_obj,
            "current_page": current_page,
            "is_paginated": paginator.count > per_page,
        },
    )


@login_required(login_url=LOGIN_URL)
def search(request):
    user = User.objects.get(username=request.user.username)
    search_term = request.GET.get("q", "").strip()

    per_page = 9

    contacts = Contact.objects.filter(
        Q(name__icontains=search_term) | Q(surname__icontains=search_term), creator=user
    ).order_by("-id")

    paginator = Paginator(contacts, 9)

    current_page = int(request.GET.get("page", 1))
    page_obj = paginator.get_page(current_page)
    page_range = utils.make_pagination(current_page, paginator.page_range, max_pages=6)

    if not search_term:
        return redirect("contacts:index")

    return render(
        request,
        "contacts/index.html",
        {
            "page_range": page_range,
            "page_obj": page_obj,
            "current_page": current_page,
            "is_paginated": paginator.count > per_page,
        },
    )


@login_required(login_url=LOGIN_URL)
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

from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView

from . import forms
from .models import Contact
from templates.static import utils


User = get_user_model()
LOGIN_URL = "accounts:login"
PER_PAGE = 9


# Create your views here.


class IndexBaseView(LoginRequiredMixin, ListView):
    model = Contact
    ordering = ["-id"]
    context_object_name = "contacts"
    template_name = "contacts/index.html"
    login_url = LOGIN_URL
    redirect_field_name = "next"

    def get_queryset(self):
        qs = super().get_queryset()
        user = User.objects.get(username=self.request.user.username)

        qs = qs.filter(creator=user)

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        page_obj, page_range, current_page = utils.make_pagination(
            request=self.request,
            queryset=context.get("contacts"),
            per_page=PER_PAGE,
        )

        context.update(
            {
                "contacts": page_obj,
                "page_range": page_range,
                "current_page": current_page,
                "is_paginated": len(page_range) > 1,
            }
        )

        return context


class SearchView(IndexBaseView):
    def get_queryset(self):
        qs = super().get_queryset()

        search_term = self.request.GET.get("q", "").strip()
        qs = qs.filter(
            Q(name__icontains=search_term) | Q(surname__icontains=search_term)
        )

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_term = self.request.GET.get("q", "").strip()

        context.update(
            {
                "search_query": f"&q={search_term}",
            }
        )

        return context


class CreateContact(LoginRequiredMixin, CreateView):
    model = Contact
    form_class = forms.CreateContactForm
    template_name = "contacts/create_contact.html"
    login_url = LOGIN_URL
    redirect_field_name = "next"

    def form_valid(self, form):
        creator = User.objects.get(username=self.request.user.username)
        contact = form.save(commit=False)
        contact.creator = creator
        contact.image = self.request.FILES.get("image")

        contact.save()

        messages.add_message(
            self.request, messages.SUCCESS, "A new contact was created!"
        )

        return redirect("contacts:index")


class ContactDetailsView(LoginRequiredMixin, DetailView):
    model = Contact
    template_name = "contacts/contact_details.html"
    login_url = LOGIN_URL
    pk_url_kwarg = "pk"
    context_object_name = "contact"

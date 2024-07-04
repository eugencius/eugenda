import re

from django import forms
from django.forms import ValidationError

from .models import Contact
from templates.static import utils


class CreateContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["description"].widget.attrs.update(
            {"container_class": "description-input"}
        )

        self.fields["category"]

        # self.fields["image"].widget.attrs.update({"container_class": "image-input"})

        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({"class": "field-input"})

    phone = forms.CharField(
        min_length=11,
        max_length=11,
    )

    class Meta:
        model = Contact
        fields = [
            "name",
            "surname",
            "phone",
            "email",
            "description",
            "image",
            "category",
        ]

    def clean_phone(self):
        phone = self.cleaned_data.get("phone")

        if re.search(r"[^0-9]", phone):
            raise ValidationError("The phone field must contain only numbers")

        return phone

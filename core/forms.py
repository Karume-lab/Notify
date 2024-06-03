from django import forms
from . import models


class Contact(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = (
            "first_name",
            "last_name",
            "phone_number",
        )


class Category(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = (
            "name",
            "description",
            "contacts_import_file",
        )


class CategoryContact(forms.ModelForm):
    class Meta:
        model = models.CategoryContact
        fields = (
            "category",
            "contact",
        )


class Message(forms.ModelForm):
    class Meta:
        model = models.Message
        fields = (
            "content",
            "category",
        )

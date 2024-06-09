from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from . import models

FORM_FIELD_STYLES = "bg-gray-50 border p-2 border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"


class Contact(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = [
            "first_name",
            "last_name",
            "phone_number",
        ]

        widgets = {
            "first_name": forms.TextInput(
                attrs={
                    "class": FORM_FIELD_STYLES,
                    "placeholder": "John",
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "class": FORM_FIELD_STYLES,
                    "placeholder": "Jones",
                }
            ),
            "phone_number": forms.NumberInput(
                attrs={
                    "class": FORM_FIELD_STYLES,
                    "placeholder": "+254712345678",
                }
            ),
        }


class Category(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = [
            "name",
            "description",
            "contacts_import_file",
        ]

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": FORM_FIELD_STYLES,
                    "placeholder": "Scientific Computing",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": FORM_FIELD_STYLES,
                    "placeholder": "Write a description about the contacts that will be stored in this category ...",
                }
            ),
        }


class CategoryContact(forms.ModelForm):
    class Meta:
        model = models.CategoryContact
        fields = [
            "category",
            "contact",
        ]


class Message(forms.ModelForm):
    class Meta:
        model = models.Message
        fields = [
            "content",
            "category",
        ]
        widgets = {
            "content": forms.Textarea(
                attrs={
                    "class": FORM_FIELD_STYLES,
                    "placeholder": "Scientific Computing",
                }
            ),
            "category": forms.Select(
                attrs={
                    "class": "form-select text-center fw-bold",
                    "style": "max-width: auto;",
                }
            ),
        }
        category = forms.ModelChoiceField(
            queryset=models.Category.objects.all(), empty_label="None"
        )

    def __init__(self, *args, **kwargs):
        super(Message, self).__init__(*args, **kwargs)
        self.fields["category"].empty_label = "None"

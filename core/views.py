import os
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from decouple import config
import pandas as pd
import africastalking as at
from . import models
from . import forms

AFRICASTALKING_USERNAME = config("DJANGO_AFRICASTALKING_USERNAME")
AFRICASTALKING_API_KEY = config("DJANGO_AFRICASTALKING_API_KEY")
at.initialize(AFRICASTALKING_USERNAME, AFRICASTALKING_API_KEY)
SMS = at.SMS


class CategoryListView(ListView):
    model = models.Category
    template_name = "categories/category_list.html"


class CategoryDetailView(DetailView):
    model = models.Category
    template_name = "categories/category_detail.html"


class CategoryCreateView(CreateView):
    model = models.Category
    form_class = forms.Category
    template_name = "categories/category_form.html"
    success_url = reverse_lazy("category-list")

    def form_valid(self, form):
        response = super().form_valid(form)
        instance = form.instance
        file_extension = os.path.splitext(instance.contacts_import_file.name)[1]

        if file_extension == ".csv":
            df = pd.read_csv(instance.contacts_import_file)
        elif file_extension == ".xlsx":
            df = pd.read_excel(instance.contacts_import_file)
        else:
            raise ValueError("Unsupported file format")

        for _, row in df.iterrows():
            try:
                contact, created = models.Contact.objects.get_or_create(
                    first_name=row["First Name"],
                    last_name=row["Sur Name"],
                    phone_number=f"+{row['Phone Number']}",
                )
                models.CategoryContact.objects.get_or_create(
                    contact=contact,
                    category=instance,
                )
            except Exception as e:
                print(f"Error importing {row['Phone Number']} {e}")
        return response


class CategoryUpdateView(UpdateView):
    model = models.Category
    form_class = forms.Category
    template_name = "categories/category_form.html"
    success_url = reverse_lazy("category-list")


class CategoryDeleteView(DeleteView):
    model = models.Category
    template_name = "categories/category_confirm_delete.html"
    success_url = reverse_lazy("category-list")


class ContactListView(ListView):
    model = models.Contact
    template_name = "contacts/contact_list.html"


class ContactDetailView(DetailView):
    model = models.Contact
    template_name = "contacts/contact_detail.html"


class ContactCreateView(CreateView):
    model = models.Contact
    form_class = forms.Contact
    template_name = "contacts/contact_form.html"
    success_url = reverse_lazy("contact-list")


class ContactUpdateView(UpdateView):
    model = models.Contact
    form_class = forms.Contact
    template_name = "contacts/contact_form.html"
    success_url = reverse_lazy("contact-list")


class ContactDeleteView(DeleteView):
    model = models.Contact
    template_name = "contacts/contact_confirm_delete.html"
    success_url = reverse_lazy("contact-list")


class MessageListView(ListView):
    model = models.Message
    template_name = "messages/message_list.html"


class MessageDetailView(DetailView):
    model = models.Message
    template_name = "messages/message_detail.html"


class MessageCreateView(CreateView):
    model = models.Message
    form_class = forms.Message
    template_name = "messages/message_form.html"
    success_url = reverse_lazy("message-list")

    def form_valid(self, form):
        response = super().form_valid(form)
        instance = form.instance
        contacts = instance.category.contacts.all()
        phone_numbers_list = [cc.contact.phone_number for cc in contacts]

        for phone_number in phone_numbers_list:
            try:
                response = SMS.send(instance.content, [str(phone_number)])
                print(response)
            except Exception as e:
                print(f"Uh oh we have a problem: {e}")

        return response


class MessageUpdateView(UpdateView):
    model = models.Message
    form_class = forms.Message
    template_name = "messages/message_form.html"
    success_url = reverse_lazy("message-list")


class MessageDeleteView(DeleteView):
    model = models.Message
    template_name = "messages/message_confirm_delete.html"
    success_url = reverse_lazy("message-list")

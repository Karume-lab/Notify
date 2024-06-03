from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User


class Contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    phone_number = PhoneNumberField(region="KE", unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Category(models.Model):
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    contacts_import_file = models.FileField(
        _("File with contacts to import"),
        upload_to="uploads/contacts/",
        max_length=100,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(
        User, related_name="categories", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class CategoryContact(models.Model):
    class Meta:
        verbose_name = "Category Contact"
        verbose_name_plural = "Category Contacts"
        unique_together = (
            "category",
            "contact",
        )

    category = models.ForeignKey(
        Category, related_name="contacts", on_delete=models.CASCADE
    )
    contact = models.ForeignKey(
        Contact,
        verbose_name=_("Contact"),
        related_name="category_contacts",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return (
            f"{self.category.name} - {self.contact.first_name} {self.contact.last_name}"
        )


class Message(models.Model):
    content = models.TextField()
    category = models.ForeignKey(
        Category, related_name="messages", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(User, related_name="messages", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.content[:30]} ..."

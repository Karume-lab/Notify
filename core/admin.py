from django.contrib import admin
from . import models


class Contact(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "phone_number",
        "created_at",
        "updated_at",
    )


class Category(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "description",
        "created_at",
        "updated_at",
    )


class CategoryContact(admin.ModelAdmin):
    list_display = (
        "id",
        "category",
        "contact",
    )


class Message(admin.ModelAdmin):
    list_display = (
        "id",
        "content",
        "category",
        "created_at",
        "sender",
    )


admin.site.register(models.Contact, Contact)
admin.site.register(models.Category, Category)
admin.site.register(models.CategoryContact, CategoryContact)
admin.site.register(models.Message, Message)

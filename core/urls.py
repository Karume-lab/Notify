from django.urls import path
from . import views

app_name = "core"
urlpatterns = [
    path("", views.home, name="home"),
    path("dashboard/", views.DashboardView.as_view(), name="dashboard"),
    path("categories/", views.CategoryListView.as_view(), name="category-list"),
    path(
        "categories/<int:pk>/",
        views.CategoryDetailView.as_view(),
        name="category-detail",
    ),
    path(
        "categories/create/", views.CategoryCreateView.as_view(), name="category-create"
    ),
    path(
        "categories/<int:pk>/update/",
        views.CategoryUpdateView.as_view(),
        name="category-update",
    ),
    path(
        "categories/<int:pk>/delete/",
        views.CategoryDeleteView.as_view(),
        name="category-delete",
    ),
    path("contacts/", views.ContactListView.as_view(), name="contact-list"),
    path(
        "contacts/<int:pk>/", views.ContactDetailView.as_view(), name="contact-detail"
    ),
    path("contacts/create/", views.ContactCreateView.as_view(), name="contact-create"),
    path(
        "contacts/<int:pk>/update/",
        views.ContactUpdateView.as_view(),
        name="contact-update",
    ),
    path(
        "contacts/<int:pk>/delete/",
        views.ContactDeleteView.as_view(),
        name="contact-delete",
    ),
    path("messages/", views.MessageListView.as_view(), name="message-list"),
    path(
        "messages/<int:pk>/", views.MessageDetailView.as_view(), name="message-detail"
    ),
    path("messages/create/", views.MessageCreateView.as_view(), name="message-create"),
    path(
        "messages/<int:pk>/update/",
        views.MessageUpdateView.as_view(),
        name="message-update",
    ),
    path(
        "messages/<int:pk>/delete/",
        views.MessageDeleteView.as_view(),
        name="message-delete",
    ),
]

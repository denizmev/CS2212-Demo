from django.urls import path

from .views import home, about, contact_view

urlpatterns = [
    path("", home),
    path("about/", about),
    path("contact/", contact_view)
]
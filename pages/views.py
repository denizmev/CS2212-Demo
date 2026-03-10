from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail

# Create your views here.

def home(request):
    return HttpResponse("Hello World")

def about(request):
    context = {"name": "Deniz",
               "players": ["Saoirse"]
               }
    return render(request, "pages/about.html", context)

def contact_view(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
            recipients = ["deniz.mevlevioglu@ucc.ie"]

            send_mail(subject, message, email, recipients)

            return render(request, "pages/contact.html", {"form": form, "success": True})

    return render(request, "pages/contact.html", {"form": form})




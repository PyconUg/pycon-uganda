from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .forms import ContactForm

# Create your views here.


# View for the Contact Page.
def contact(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]
            try:
                send_mail(subject, message, email, ['admin@example.com'], name)
            except BadHeaderError:
                return HttpResponse("Invalid header found")
            return redirect("email_success")
    return render(request, 'contact.html', {"form": form})
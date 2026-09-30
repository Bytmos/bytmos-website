from django.shortcuts import render
from datetime import datetime
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import reverse
from django.views.generic import TemplateView, FormView


# Create your views here.
def home(request):
    context = {
        'year': datetime.now().year
    }
    return render(request, 'personal/index.html', context)


def bytmos_partner(request):
    return render(request, 'personal/partner.html')


def about(request):
    return render(request, 'personal/about-us.html')


def faqs(request):
    return render(request, 'personal/faqs.html')


def terms(request):
    return render(request, 'personal/terms.html')


def privacy(request):
    return render(request, 'personal/privacy.html')

def account_deletion(request):
    return render(request, 'personal/account_deletion.html')


# def contact(request):
#     return render(request, 'personal/contact-us.html')
class GoogleVerificationView(TemplateView):
    template_name = 'personal/googlec25e06cc20399bc4.html'


class SuccessView(TemplateView):
    template_name = "success.html"


class ContactView(FormView):
    form_class = ContactForm
    template_name = "personal/contact-us.html"

    def get_success_url(self):
        return reverse("contact")

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        subject = form.cleaned_data.get("subject")
        message = form.cleaned_data.get("message")

        full_message = f"""
            Received message below from {email}, {subject}
            ________________________


            {message}
            """
        send_mail(
            subject="Received contact form submission",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.NOTIFY_EMAIL],
        )
        return super(ContactView, self).form_valid(form)
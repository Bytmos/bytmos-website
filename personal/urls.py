from django.urls import path

from .views import SuccessView, ContactView, GoogleVerificationView

urlpatterns = [
    path("contact/", ContactView.as_view(), name="contact"),
    path("success/", SuccessView.as_view(), name="success"),
    path('googlec25e06cc20399bc4.html', GoogleVerificationView.as_view(), name='google_verification'),
]
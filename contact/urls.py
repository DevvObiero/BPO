# contact/urls.py
from django.urls import path
from .views import ContactSubmissionCreateView

urlpatterns = [
    path('submit-contact/', ContactSubmissionCreateView.as_view(), name='submit-contact'),
]
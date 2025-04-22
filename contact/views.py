from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import ContactSubmission
from .serializers import ContactSubmissionSerializer

# contact/views.py
class ContactSubmissionCreateView(generics.CreateAPIView):
    queryset = ContactSubmission.objects.all()
    serializer_class = ContactSubmissionSerializer
    permission_classes = [AllowAny] # Allow unauthenticated users to submit

    def perform_create(self, serializer):
        # You can add logic here to send an email notification
        # to the company when a new submission is created.
        serializer.save()
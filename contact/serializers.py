# contact/serializers.py
from rest_framework import serializers
from .models import ContactSubmission

class ContactSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactSubmission
        fields = '__all__'
        read_only_fields = ['submitted_at'] # Make submitted_at automatically set
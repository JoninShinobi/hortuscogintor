from django import forms
from django.core.exceptions import ValidationError
from django.utils.html import strip_tags
import re
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['full_name', 'email', 'phone', 'message']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'placeholder': 'Your Full Name',
                'maxlength': '100',
                'pattern': '[A-Za-z\\s\\-\\.\']+',
                'title': 'Please enter a valid name (letters, spaces, hyphens, periods, and apostrophes only)'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'your@email.com',
                'maxlength': '254'
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': 'Your Phone Number (Optional)',
                'maxlength': '20',
                'pattern': '[0-9\\s\\+\\-\\(\\)]+',
                'title': 'Please enter a valid phone number'
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Any questions or special requirements?',
                'rows': 4,
                'maxlength': '1000'
            }),
        }
    
    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name', '').strip()
        
        # Length validation
        if len(full_name) < 2:
            raise ValidationError("Name must be at least 2 characters long.")
        if len(full_name) > 100:
            raise ValidationError("Name must be less than 100 characters.")
        
        # Character validation - only letters, spaces, hyphens, periods, apostrophes
        if not re.match(r"^[A-Za-z\s\-\.']+$", full_name):
            raise ValidationError("Name can only contain letters, spaces, hyphens, periods, and apostrophes.")
        
        # Strip any HTML tags as additional security
        full_name = strip_tags(full_name)
        
        return full_name
    
    def clean_email(self):
        email = self.cleaned_data.get('email', '').strip().lower()
        
        # Strip HTML tags
        email = strip_tags(email)
        
        # Additional email validation
        if len(email) > 254:
            raise ValidationError("Email address is too long.")
            
        return email
    
    def clean_phone(self):
        phone = self.cleaned_data.get('phone', '').strip()
        
        if phone:  # Only validate if phone is provided (it's optional)
            # Strip HTML tags
            phone = strip_tags(phone)
            
            # Remove all non-digit characters for length check
            digits_only = re.sub(r'[^0-9]', '', phone)
            
            # Length validation
            if len(digits_only) < 6:
                raise ValidationError("Phone number must contain at least 6 digits.")
            if len(digits_only) > 15:
                raise ValidationError("Phone number must contain no more than 15 digits.")
            
            # Character validation - only numbers, spaces, +, -, (, )
            if not re.match(r"^[0-9\s\+\-\(\)]+$", phone):
                raise ValidationError("Phone number can only contain numbers, spaces, +, -, (, and ).")
        
        return phone
    
    def clean_message(self):
        message = self.cleaned_data.get('message', '').strip()
        
        # Strip HTML tags to prevent XSS
        message = strip_tags(message)
        
        # Length validation
        if len(message) > 1000:
            raise ValidationError("Message must be less than 1000 characters.")
        
        # Check for potential script injection attempts
        dangerous_patterns = [
            r'<script',
            r'javascript:',
            r'onclick=',
            r'onerror=',
            r'onload=',
            r'eval\(',
            r'document\.',
            r'window\.',
        ]
        
        message_lower = message.lower()
        for pattern in dangerous_patterns:
            if re.search(pattern, message_lower):
                raise ValidationError("Message contains potentially unsafe content.")
        
        return message
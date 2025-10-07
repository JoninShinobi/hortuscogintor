from django.db import models
from django.utils.text import slugify
from django.core.validators import RegexValidator, MinLengthValidator, MaxLengthValidator
from django.core.exceptions import ValidationError
import re

class Course(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300, blank=True)
    hero_image = models.ImageField(upload_to='courses/hero_images/', blank=True, null=True, help_text='Recommended size: 1920x1080px (16:9 aspect ratio)')
    description = models.TextField()
    what_you_will_experience = models.TextField()
    course_structure = models.TextField()
    location = models.TextField()
    accessibility = models.TextField()
    who_this_is_for = models.TextField()
    what_you_will_gain = models.TextField()
    start_date = models.DateField()
    duration = models.CharField(max_length=100)
    max_participants = models.IntegerField(default=15)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    slug = models.SlugField(unique=True, max_length=200, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['start_date']

class Instructor(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    photo = models.ImageField(upload_to='instructors/', blank=True, null=True)
    courses = models.ManyToManyField(Course, related_name='instructors')
    
    def __str__(self):
        return self.name

def validate_no_html(value):
    """Validator to prevent HTML/script injection"""
    if re.search(r'<[^>]*>', value):
        raise ValidationError('HTML tags are not allowed.')
    
    dangerous_patterns = [
        r'javascript:', r'onclick=', r'onerror=', r'onload=',
        r'eval\(', r'document\.', r'window\.'
    ]
    
    value_lower = value.lower()
    for pattern in dangerous_patterns:
        if re.search(pattern, value_lower):
            raise ValidationError('Potentially unsafe content detected.')

class Booking(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='bookings')
    full_name = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(2, "Name must be at least 2 characters long."),
            RegexValidator(
                regex=r'^[A-Za-z\s\-\.\''']+$',
                message='Name can only contain letters, spaces, hyphens, periods, and apostrophes.'
            ),
            validate_no_html
        ],
        help_text="Full name (2-100 characters, letters only)"
    )
    email = models.EmailField(
        max_length=254,
        validators=[validate_no_html],
        help_text="Valid email address"
    )
    phone = models.CharField(
        max_length=20,
        blank=True,
        validators=[
            RegexValidator(
                regex=r'^[0-9\s\+\-\(\)]*$',
                message='Phone number can only contain numbers, spaces, +, -, (, and ).'
            ),
            validate_no_html
        ],
        help_text="Optional phone number"
    )
    message = models.TextField(
        blank=True,
        max_length=1000,
        validators=[validate_no_html],
        help_text="Optional message (maximum 1000 characters)"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    def clean(self):
        """Additional model-level validation"""
        super().clean()
        
        # Validate phone number has sufficient digits if provided
        if self.phone:
            digits_only = re.sub(r'[^0-9]', '', self.phone)
            if len(digits_only) < 6:
                raise ValidationError({'phone': 'Phone number must contain at least 6 digits.'})
            if len(digits_only) > 15:
                raise ValidationError({'phone': 'Phone number must contain no more than 15 digits.'})
    
    def save(self, *args, **kwargs):
        """Override save to run full_clean validation"""
        self.full_clean()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.full_name} - {self.course.title}"
    
    class Meta:
        ordering = ['-created_at']
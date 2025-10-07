from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.core.cache import cache
from django.http import HttpResponseForbidden
from django.utils import timezone
from datetime import timedelta
import hashlib
from .models import Course, Instructor, Booking
from .forms import BookingForm

def home(request):
    featured_courses = Course.objects.filter(is_active=True)[:3]
    context = {
        'featured_courses': featured_courses
    }
    return render(request, 'home.html', context)

def regenerative_movement_course(request):
    return render(request, 'regenerative_movement_course.html')

class CourseListView(ListView):
    model = Course
    template_name = 'courses/course_list.html'
    context_object_name = 'courses'
    
    def get_queryset(self):
        return Course.objects.filter(is_active=True)

class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/course_detail.html'
    context_object_name = 'course'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['booking_form'] = BookingForm()
        return context

def get_client_ip(request):
    """Get client IP address for rate limiting"""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def is_rate_limited(request, action='booking', limit=3, window=300):
    """
    Rate limiting function
    - limit: max attempts per window
    - window: time window in seconds (default 5 minutes)
    """
    ip = get_client_ip(request)
    cache_key = f'rate_limit_{action}_{ip}'
    
    attempts = cache.get(cache_key, 0)
    if attempts >= limit:
        return True
    
    cache.set(cache_key, attempts + 1, window)
    return False

def book_course(request, slug):
    course = get_object_or_404(Course, slug=slug)
    
    if request.method == 'POST':
        # Rate limiting - max 3 booking attempts per 5 minutes per IP
        if is_rate_limited(request, 'booking', limit=3, window=300):
            messages.error(request, 'Too many booking attempts. Please wait 5 minutes before trying again.')
            return redirect('course_detail', slug=course.slug)
        
        form = BookingForm(request.POST)
        if form.is_valid():
            try:
                booking = form.save(commit=False)
                booking.course = course
                booking.save()
                messages.success(request, f'Thank you for booking {course.title}! We will contact you soon.')
                return redirect('course_detail', slug=course.slug)
            except Exception as e:
                messages.error(request, 'There was an error processing your booking. Please try again.')
                return redirect('course_detail', slug=course.slug)
        else:
            # Form validation failed
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field.replace("_", " ").title()}: {error}')
    else:
        form = BookingForm()
    
    return render(request, 'courses/course_detail.html', {
        'course': course,
        'booking_form': form
    })
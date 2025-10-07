from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Course, Instructor, Booking

@admin.register(Course)
class CourseAdmin(ModelAdmin):
    list_display = ['title', 'start_date', 'duration', 'price', 'max_participants', 'is_active']
    list_filter = ['is_active', 'start_date']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'start_date'
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'subtitle', 'slug', 'is_active')
        }),
        ('Hero Section', {
            'fields': ('hero_image',),
            'description': 'Hero background image for course pages. Recommended size: 1920x1080px (16:9 aspect ratio).'
        }),
        ('Course Details', {
            'fields': ('description', 'what_you_will_experience', 'course_structure'),
            'classes': ('collapse',)
        }),
        ('Logistics', {
            'fields': ('location', 'accessibility'),
            'classes': ('collapse',)
        }),
        ('Target Audience & Benefits', {
            'fields': ('who_this_is_for', 'what_you_will_gain'),
            'classes': ('collapse',)
        }),
        ('Scheduling & Pricing', {
            'fields': ('start_date', 'duration', 'max_participants', 'price')
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
            'description': 'Automatically managed timestamps.'
        })
    )
    
    readonly_fields = ['created_at', 'updated_at']
    
    # Media removed - using Django Unfold's global styles instead

@admin.register(Instructor)
class InstructorAdmin(ModelAdmin):
    list_display = ['name', 'photo_preview', 'course_count']
    search_fields = ['name', 'bio']
    filter_horizontal = ['courses']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'photo')
        }),
        ('Biography', {
            'fields': ('bio',),
            'description': 'Detailed biography to display on course pages.'
        }),
        ('Courses', {
            'fields': ('courses',),
            'description': 'Select which courses this instructor teaches.'
        })
    )
    
    def photo_preview(self, obj):
        if obj.photo:
            return f'<img src="{obj.photo.url}" style="width: 50px; height: 50px; border-radius: 50%; object-fit: cover;">'
        return "No photo"
    photo_preview.allow_tags = True
    photo_preview.short_description = "Photo"
    
    def course_count(self, obj):
        return obj.courses.count()
    course_count.short_description = "Courses"
    
@admin.register(Booking)
class BookingAdmin(ModelAdmin):
    list_display = ['full_name', 'email', 'course', 'created_at']
    list_filter = ['course', 'created_at']
    search_fields = ['full_name', 'email', 'course__title']
    date_hierarchy = 'created_at'
    readonly_fields = ['created_at']
    
    fieldsets = (
        ('Contact Information', {
            'fields': ('full_name', 'email', 'phone')
        }),
        ('Booking Details', {
            'fields': ('course', 'message', 'created_at')
        })
    )
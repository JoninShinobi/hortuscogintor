from django.urls import path
from . import views

urlpatterns = [
    path('', views.CourseListView.as_view(), name='course_list'),
    path('<slug:slug>/', views.CourseDetailView.as_view(), name='course_detail'),
    path('<slug:slug>/book/', views.book_course, name='book_course'),
]
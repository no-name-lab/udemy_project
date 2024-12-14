from django_filters.rest_framework import FilterSet
from .models import Course


class CourseFilter(FilterSet):
    class Meta:
        model = Course
        fields = {
            'price': ['gt', 'lt'],
            'category': ['exact'], 
        }
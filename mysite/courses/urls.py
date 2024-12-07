from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'users', UserProfileViewSet, basename='user-list')
router.register(r'courses', CourseViewSet, basename='course-list')
router.register(r'lessons', LessonViewSet, basename='lesson-list')
router.register(r'assignments', AssignmentViewSet, basename='assignment-list')
router.register(r'exams', ExamViewSet, basename='exam-list')


urlpatterns = [
    path('', include(router.urls))
]


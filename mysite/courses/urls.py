from .views import *
from rest_framework import routers
from django.urls import path, include


router = routers.SimpleRouter()

router.register(r'user', UserProfileViewSet, basename='user_list')
router.register(r'course', CourseViewSet, basename='course')
router.register(r'lesson', LessonViewSet, basename='lesson')
router.register(r'assignment', AssignmentViewSet, basename='assignment')
router.register(r'exam_questions', ExamQuestionsViewSet, basename='exam_questions')
router.register(r'exam', ExamViewSet, basename='exam')
router.register(r'certificate', CertificateViewSet, basename='certificate')
router.register(r'review', ReviewViewSet, basename='review')


urlpatterns = [
    path('', include(router.urls)),

]
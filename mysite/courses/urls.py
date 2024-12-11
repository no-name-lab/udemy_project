from .views import *
from rest_framework import routers
from django.urls import path, include


router = routers.SimpleRouter()

router.register(r'user', UserProfileViewSet, basename='user_list')
router.register(r'lesson', LessonViewSet, basename='lesson')
router.register(r'assignment', AssignmentViewSet, basename='assignment')
router.register(r'exam_questions', ExamQuestionsViewSet, basename='exam_questions')
router.register(r'exam', ExamViewSet, basename='exam')
router.register(r'certificate', CertificateViewSet, basename='certificate')
router.register(r'review', ReviewViewSet, basename='review')


urlpatterns = [
    path('', include(router.urls)),
    path('course/', CourseListApiViewViewSet.as_view(), name='course_list'),
    path('course/<int:pk>/', CourseDetailApiViewViewSet.as_view(), name='course_detail'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
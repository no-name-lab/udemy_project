from rest_framework import viewsets, generics
from .serializers import *
from .models import *


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class CourseListApiViewViewSet(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseListSerializer
    
    
class CourseDetailApiViewViewSet(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer



class ExamQuestionsViewSet(viewsets.ModelViewSet):
    queryset = ExamQuestions.objects.all()
    serializer_class = ExamQuestionsSerializer



class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer


class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

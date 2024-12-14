from rest_framework import viewsets, generics, status
from .serializers import *
from .models import *
# from .permissions import IsAdmin, IsTeacher, IsStudent, IsOwnerOrAdmin
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from django_filters.rest_framework import DjangoFilterBackend
from .filters import CourseFilter
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter


class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CustomLoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response({"detail": "Неверные учетные данные"}, status=status.HTTP_401_UNAUTHORIZED)

        user = serializer.validated_data
        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutView(generics.GenericAPIView):
    def post(self, request, **kwargs):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except KeyError:
            return Response({"detail": "Требуется refresh-токен."}, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)



class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    # permission_classes = [IsAdmin]


class CourseListApiViewViewSet(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = CourseFilter
    search_fields = ['course_name']
    ordering_fields = ['price']



class CourseDetailApiViewViewSet(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = CourseFilter
    search_fields = ['course_name']
    ordering_fields = ['price']


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    # permission_classes = [IsAdmin, IsTeacher]


class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    # permission_classes = [IsAdmin, IsTeacher]


class ExamQuestionsViewSet(viewsets.ModelViewSet):
    queryset = ExamQuestions.objects.all()
    serializer_class = ExamQuestionsSerializer
    # permission_classes = [IsAdmin, IsTeacher]


class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    # permission_classes = [IsAdmin, IsTeacher]


class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    # permission_classes = [IsAdmin, IsOwnerOrAdmin]


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    # permission_classes = [IsStudent, IsTeacher]

from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate 


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'username']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['title', 'video_url', 'content', 'course']


class CourseListSerializer(serializers.ModelSerializer):
    avg_rating = serializers.SerializerMethodField()
    discount_info = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ['course_name', 'price', 'avg_rating', 'discount_info']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_discount_info(self, obj):
        return obj.get_discount_info()


class CourseDetailSerializer(serializers.ModelSerializer):
    avg_rating = serializers.SerializerMethodField()
    reviews = ReviewSerializer(many=True, read_only=True)  # Используйте ReviewSerializer
    course_lessons = LessonSerializer(many=True, read_only=True)
    class Meta:
        model = Course
        fields = ['id', 'course_name', 'description', 'category', 'level', 'price',
                  'avg_rating', 'created_at', 'updated_at', 'course_lessons',
                  'reviews']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ['title', 'description', 'due_date', 'course', 'students']


class ExamQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamQuestions
        fields = ['questions_name', 'questions']


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ['title', 'course', 'questions', 'passing_score', 'duration']


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ['student', 'course', 'issued_at', 'certificate_url']




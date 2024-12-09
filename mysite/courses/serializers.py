from rest_framework import serializers
from .models import *


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'username']



class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class CourseListSerializer(serializers.ModelSerializer):
    avg_rating = serializers.SerializerMethodField()
    class Meta:
        model = Course
        fields = ['course_name', 'price', 'avg_rating']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()


class CourseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['course_name', 'description',
                  'category', 'level', 'price', 'created_at']


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['title', 'video_url', 'content', 'course_url']


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


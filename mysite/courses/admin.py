from django.contrib import admin
from .models import *
from .views import CertificateViewSet

admin.site.registerL(UserProfile)
admin.site.registerL(Lesson)
admin.site.registerL(Assignment)
admin.site.registerL(ExamQuestions)
admin.site.registerL(Exam)
admin.site.registerL(CertificateViewSet)
admin.site.registerL(Review)

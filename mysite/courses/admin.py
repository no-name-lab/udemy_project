from django.contrib import admin
from .models import *
from .views import *

admin.site.register(UserProfile)
admin.site.register(Lesson)
admin.site.register(Assignment)
admin.site.register(ExamQuestions)
admin.site.register(Exam)
admin.site.register(CertificateViewSet)
admin.site.register(Review)

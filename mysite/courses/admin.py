from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin

@admin.register(Course)
class AllAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }



admin.site.register(UserProfile)
admin.site.register(Lesson)
admin.site.register(Assignment)
admin.site.register(ExamQuestions)
admin.site.register(Exam)
admin.site.register(Certificate)
admin.site.register(Review)

from modeltranslation.translator import TranslationOptions, register
from .models import *

@register(Course)
class CourseTranslationOptions(TranslationOptions):
    fields = ('course_name', 'description')

@register(Lesson)
class LessonTranslationOptions(TranslationOptions):
    fields = ('title', 'content')

@register(Assignment)
class AssignmentTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(ExamQuestions)
class ExamQuestionsTranslationOptions(TranslationOptions):
    fields = ('questions_name', 'questions')

@register(Exam)
class ExamTranslationOptions(TranslationOptions):
    fields = ('title',)

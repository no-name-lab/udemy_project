from django.db import models
from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
    ROLE_CHOICES = [
        ('Клиент', 'Клиент'),
        ('Преподаватель', 'Преподаватель'),
        ('Администратор', 'Администратор'),
    ]

    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Клиент')
    full_name = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

class Course(models.Model):
    CATEGORY_CHOICES = [
        ('Программирование', 'Программирование'),
        ('Маркетинг', 'Маркетинг'),
        ('Дизайн', 'Дизайн'),
    ]
    LEVEL_CHOICES = [
        ('Начальный', 'Начальный'),
        ('Средний', 'Средний'),
        ('Продвинутый', 'Продвинутый'),
    ]
    course_name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    level = models.CharField(max_length=15, choices=LEVEL_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    original_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.course_name

    def get_avg_rating(self):
        ratings = self.reviews.all()
        if ratings.exists():
            return round(sum(i.rating for i in ratings) / ratings.count(), 1)
        return 0

    def get_discount_info(self):
        if self.original_price and self.price:
            discount = (self.original_price - self.price) / self.original_price * 100
            return {
                "original_price": f"{self.original_price:.2f} $",
                "discount": f"{discount:.0f}%",
                "current_price": f"{self.price:.2f} $"
            }
        return {
            "original_price": None,
            "discount": "0%",
            "current_price": f"{self.price:.2f} $"
        }


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_lessons')
    title = models.CharField(max_length=30)
    video_url = models.FileField(upload_to='vid/')
    content = models.TextField()



class Assignment(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField()
    due_date = models.CharField(max_length=50)
    course = models.URLField()
    students = models.URLField()

class ExamQuestions(models.Model):
    questions_name = models.CharField(max_length=32)
    questions = models.TextField()

class Exam(models.Model):
    title = models.CharField(max_length=32)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    questions = models.ForeignKey(ExamQuestions, on_delete=models.CASCADE)
    passing_score = models.PositiveSmallIntegerField()
    duration = models.PositiveSmallIntegerField()

class Certificate(models.Model):
    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    issued_at = models.DateTimeField()
    certificate_url = models.URLField()

class Review(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='reviews')  
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comment = models.TextField()


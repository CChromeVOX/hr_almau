from django.db import models
from django.contrib.auth.models import User

class Faculty(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=50)
    level = models.CharField(max_length=20)  

    def __str__(self):
        return self.name

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, null=True)
    course = models.IntegerField(null=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True)  # Assuming you'll upload photos to a directory named 'profile_photos'
    github = models.URLField(null=True)
    languages = models.ManyToManyField(Language, through='StudentLanguage')  # Many-to-Many relationship with Language through StudentLanguage

    def __str__(self):
        return self.user.username
    
class StudentLanguage(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    proficiency_level = models.CharField(max_length=20)  # Proficiency level of the student in the language

    def __str__(self):
        return f"{self.student.user.username}'s {self.language.name} proficiency: {self.proficiency_level}"
    

class Project(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to='project_photos/')  # Папка для хранения фотографий проектов

    def __str__(self):
        return self.title

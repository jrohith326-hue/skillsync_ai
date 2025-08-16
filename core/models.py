from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    interests = models.TextField(blank=True, null=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)

    def __str__(self):
        return self.user.username

class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Interest(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CareerPath(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    required_skills = models.ManyToManyField(Skill)

    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    related_skills = models.ManyToManyField(Skill)

    def __str__(self):
        return self.title




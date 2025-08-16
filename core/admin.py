from django.contrib import admin
from .models import UserProfile, Skill, Interest, CareerPath, Course

admin.site.register(UserProfile)
admin.site.register(Skill)
admin.site.register(Interest)
admin.site.register(CareerPath)
admin.site.register(Course)

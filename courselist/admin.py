from django.contrib import admin
from .models import Term, Course, UserCourse

admin.site.register(Term)
admin.site.register(Course)
admin.site.register(UserCourse)

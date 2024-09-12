from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Term(models.Model):
    SESSION_CHOICES = [('w', 'Winter'), ('s', 'Summer'),]
    TERM_CHOICES = [(1, 'Term 1'), (1, 'Term 2')]

    year = models.IntegerField()
    session = models.CharField(max_length=1, choices=SESSION_CHOICES)
    term = models.PositiveSmallIntegerField(choices=TERM_CHOICES)

    def __str__(self):
        return f'{self.year} {self.session}T{self.term}'


class Course(models.Model):
    subject = models.CharField(max_length=10)
    number = models.IntegerField()
    # full_course_name = models.CharField(max_length=100, null=True, blank=True)
    credits = models.IntegerField(default=3)
    # terms_offered = models.ManyToManyField(Term, help_text='Select the terms in which the course is offered.')
    # is_science_credit = models.BooleanField()

    def __str__(self):
        return f'{self.subject} {self.number}'
    
    class Meta:
        unique_together = ('subject', 'number')

class UserCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.course} ({self.order})'

    class Meta:
        unique_together = [('user', 'course'), ('user', 'order')]

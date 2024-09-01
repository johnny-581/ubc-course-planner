from django.db import models
from django.urls import reverse


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
    full_course_name = models.CharField(max_length=100, null=True, blank=True)
    terms_offered = models.ManyToManyField(Term, help_text='Select the terms in which the course is offered.')

    def __str__(self):
        return f'{self.subject} {self.number}'
    class Meta:
        unique_together = ('subject', 'number')
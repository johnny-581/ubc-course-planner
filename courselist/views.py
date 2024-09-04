from django.shortcuts import render
from .models import Course
from django.db.models import Sum

def index(request):
    num_courses = Course.objects.count()
    total_credits = Course.objects.aggregate(Sum('credits'))['credits__sum'] or 0

    context = {
        'num_courses': num_courses,
        'total_credits': total_credits,
    }

    return render(request, 'index.html', context=context)
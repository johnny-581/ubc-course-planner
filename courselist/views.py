from django.shortcuts import render
from .models import Course, UserCourse
from django.db.models import Sum
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

def index(request):
    num_courses = Course.objects.count()
    total_credits = Course.objects.aggregate(Sum('credits'))['credits__sum'] or 0

    context = {
        'num_courses': num_courses,
        'total_credits': total_credits,
    }

    return render(request, 'index.html', context=context)

class CoursesByUserListView(LoginRequiredMixin, generic.ListView):
    model = UserCourse
    template_name = 'user_courses.html'
    context_object_name = 'user_courses'

    def get_queryset(self):
        return UserCourse.objects.filter(user=self.request.user).select_related('course').order_by('order')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_total_credits = (UserCourse.objects.filter(user=self.request.user)
                              .aggregate(Sum('course__credits'))['course__credits__sum'] or 0)
        
        context['user_total_credits'] = user_total_credits

        return context

from django.shortcuts import render, get_object_or_404
from courses.models import Course

def home_view(request):
    courses = Course.objects.all()
    context = {'courses': courses }
    return render(request, 'home.html',context)

def detail_view(request,pid):
    course = get_object_or_404(Course ,pk=pid ,status=True)
    context = {'course':course}
    return render(request, 'detail.html',context)

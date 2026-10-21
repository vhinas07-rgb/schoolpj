
from django.shortcuts import render, get_object_or_404
from courses.models import Course, Category


def home_view(request):
    category_id = request.GET.get('category')

    if category_id:
        courses = Course.objects.filter(category__id=category_id)
    else:
        courses = Course.objects.all()

    return render(request, 'home.html', {
        'courses': courses,
        'categories': Category.objects.all(),
    })


def detail_view(request,pid):
    course = get_object_or_404(Course ,pk=pid ,status=True)
    context = {'course':course}
    return render(request, 'detail.html',context)

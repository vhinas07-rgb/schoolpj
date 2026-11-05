from django.shortcuts import render, get_object_or_404, redirect
from .forms import CourseForm, ContactForm
from .models import Course, Category


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
#مدل course

def form_view(request, pid=None):

    if pid:
        course = get_object_or_404(Course, pk=pid)
    else:
        course = None

    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)
        
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = CourseForm(instance=course)

    return render(
        request,
        'form.html',{'form': form, 'course': course})

def delete_view(request, pid):
    course = get_object_or_404(Course, pk=pid)

    if request.method == 'POST':
        course.delete()
        return redirect('home')

    return render(request, 'course_confirm_delete.html', {
        'course': course
    })

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')

    return redirect('home')
   

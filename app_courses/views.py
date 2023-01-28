from django.shortcuts import render
from .models import Course

# Create your views here.
def courses(request):
    all_courses = Course.objects.all()
    context = {'all_courses': all_courses}
    return render(request, 'app_courses/courses.html', context)

def course(request, course_id):
    one_course = None
    try:
        one_course = Course.objects.get(refcode=course_id)
    except:
        print("ไม่พบคอร์ส")
    context = {'course': one_course}
    return render(request, 'app_courses/course.html',context)
from django.shortcuts import render

# Create your views here.
def courses(request):
    return render(request, 'app_courses/courses.html')

def course(request, course_id):
    return render(request, 'app_courses/course.html',context={'course_id': course_id})
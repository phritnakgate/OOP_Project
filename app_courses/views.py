from django.shortcuts import render

all_courses = [
    {'id':'c_programming', 'title': 'Fundamental C Programming', 'teacher': 'A.Thanunchai'},
    {'id':'arduino', 'title': 'Fundamental Arduino', 'teacher': 'A.Thana'},
    {'id':'java_programming', 'title': 'Fundamental Java Programming', 'teacher': 'P.Boss'}
]

# Create your views here.
def courses(request):
    context = {'all_courses': all_courses}
    return render(request, 'app_courses/courses.html', context)

def course(request, course_id):
    return render(request, 'app_courses/course.html',context={'course_id': course_id})
from django.shortcuts import render

all_courses = [
    {'id': 1, 'title': 'Fundamental C Programming', 'teacher': 'A.Thanunchai'},
    {'id': 2, 'title': 'Fundamental Arduino', 'teacher': 'A.Thana'},
    {'id': 3, 'title': 'Fundamental Java Programming', 'teacher': 'P.Boss'}
]

# Create your views here.
def courses(request):
    context = {'all_courses': all_courses}
    return render(request, 'app_courses/courses.html', context)

def course(request, course_id):
    one_course = None
    try:
        one_course = [f for f in all_courses if f['id'] == course_id][0]
    except IndexError:
        print("ไม่พบคอร์ส")
    context = {'course': one_course}
    return render(request, 'app_courses/course.html',context)
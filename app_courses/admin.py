from django.contrib import admin
from app_courses.models import Course

# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ['title','refcode','catg']
    search_fields = ['title']
    list_filter = ['catg']

admin.site.register(Course, CourseAdmin)
from django.contrib import admin
from .models import Student, Faculty, Course, Department, Assignment, Announcement

class CourseAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'faculty_name', 'view_students']

    def faculty_name(self, obj):
        # Get the faculty associated with this course
        faculty = obj.faculty
        return faculty.name if faculty else None

    def view_students(self, obj):
        # Get the list of students enrolled in this course
        students = obj.students.all()
        # Format the list of student names
        student_list = ', '.join([student.name for student in students])
        return student_list

    faculty_name.short_description = 'Faculty'

    view_students.short_description = 'Students Enrolled'

admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(Course, CourseAdmin)
admin.site.register(Department)
admin.site.register(Assignment)
admin.site.register(Announcement) 
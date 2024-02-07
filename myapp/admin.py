from django.contrib import admin
from myapp.models import*
# Register your models here.

admin.site.register(AddJobTable)
admin.site.register(CourseTable)
admin.site.register(StudentTable)
admin.site.register(MarksTable)
admin.site.register(GradeTable)
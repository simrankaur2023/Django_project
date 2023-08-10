from django.contrib import admin
from app1.models import students , teacher ,classroom,marks

admin.site.register(students)
admin.site.register(classroom)
admin.site.register(teacher)
admin.site.register(marks)



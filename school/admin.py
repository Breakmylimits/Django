from django.contrib import admin
from .models import ExamScore, Allstudent, Profile, DocumentUpload

admin.site.register(ExamScore)

class StudentAdmin(admin.ModelAdmin):
    list_display = ['level','student_id','student_name','student_tel']
    list_filter = ['level']
    list_editable = ['student_name','student_id']


admin.site.register(Allstudent, StudentAdmin)
admin.site.register(Profile)
admin.site.register(DocumentUpload)


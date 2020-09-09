from django.contrib import admin
from News_app.models import employee

# Register your models here.
class employeeAdmin(admin.ModelAdmin):
    list_display = ['emp_num','emp_name','emp_sal','emp_dept','emp_add']


admin.site.register(employee,employeeAdmin)

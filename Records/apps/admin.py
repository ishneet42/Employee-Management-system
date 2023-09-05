from django.contrib import admin
from .models import Employee
from import_export.admin import ImportExportModelAdmin

class EmployeeAdmin(ImportExportModelAdmin):
    list_display = [
        'emp_id',
        'emp_name',
        'emp_department',
        'emp_office_loc',
        'att_date',
        'in_time',
        'out_time',
    ]

admin.site.register(Employee, EmployeeAdmin)

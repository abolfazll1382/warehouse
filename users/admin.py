# MY_DJANGO PROJECTS TRAINING/warehouse_erp/users/admin.py

from django.contrib import admin
from users.models import Department, EmployeeProfile


admin.site.register(Department)
admin.site.register(EmployeeProfile)
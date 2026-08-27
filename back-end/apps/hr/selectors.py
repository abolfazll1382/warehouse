from apps.hr.models import Employee, Payroll


def employee_list(*, department: str | None = None, status: str | None = None):
    qs = Employee.objects.all()
    if department:
        qs = qs.filter(department=department)
    if status:
        qs = qs.filter(status=status)
    return qs


def payroll_list(*, employee_id: int | None = None):
    qs = Payroll.objects.select_related("employee")
    if employee_id:
        qs = qs.filter(employee_id=employee_id)
    return qs

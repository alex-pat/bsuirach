from django.shortcuts import render_to_response
from employees.models import Employee
from . import tops

def index(request):
    tops.update_users()
    tops.update_employees()
    employees = Employee.objects.order_by('lastName')
    return render_to_response('home/index.html', {
        'employees': employees,
        'username': request.user.username,
        'top_employees': tops.TOP_EMPLOYEES,
        'top_users': tops.TOP_USERS,
    })

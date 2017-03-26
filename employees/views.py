from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test
from .models import Employee
from .bsuirapi import get_employees


def show(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    return render(request, 'employees/show.html', {'employee': employee, 'username': request.user.username})


@user_passes_test(lambda u: u.is_superuser)
def update(request):
    employees = get_employees()
    for empl in employees:
        employee, _ = Employee.objects.get_or_create(bsuir_id=int(empl['id']))
        employee.academicDepartment = empl['academicDepartment']
        employee.calendarId = empl['calendarId']
        employee.firstName = empl['firstName']
        employee.lastName = empl['lastName']
        employee.middleName = empl['middleName']
        employee.photoLink = empl['photoLink']
        employee.description = empl['rank']
        employee.save()
    return redirect('/')

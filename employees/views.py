from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from images.forms import ImageForm
from .models import Employee
from .bsuirapi import get_employees


def show(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    form = ImageForm()
    context =  {
        'employee': employee,
        'username': request.user.username,
        'image_form': form
    }
    return render(request, 'employees/show.html', context)


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
    return HttpResponse("Success")

def add_tags(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    employee.tags.add(*request.GET['tags'].split())
    employee.save()
    return redirect('/employees/{}/'.format(employee_id))

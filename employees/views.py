from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee


def show(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    return render(request, 'employees/show.html', {'employee': employee, 'username': request.user.username})

def update(request):
    pass

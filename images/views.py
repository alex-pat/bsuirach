from django.shortcuts import render, get_object_or_404, redirect
from employees.models import Employee
from images.forms import ImageForm
import cloudinary

cloudinary.config(
  cloud_name = "alex-pat-test-cloud",
  api_key = "341293339266712",
  api_secret = "TJqWJMB4ClL9Sqt6MPKd4Ts5zGE"
)

def create(request):
    form = ImageForm(request.POST, request.FILES)
    if form.is_valid():
        image = form.save()
        employee = get_object_or_404(Employee, pk=request.POST['employee_id'])
        employee.images.add(image)
        employee.save()
        return redirect('/')

    return redirect('/')

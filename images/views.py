from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
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
    employee_id = request.POST['employee_id']
    if form.is_valid():
        image = form.save()
        employee = get_object_or_404(Employee, pk=employee_id)
        employee.images.add(image)
        employee.save()
        return redirect('/employees/{}/'.format(employee_id))

    return redirect('/employees/{}/'.format(employee_id))


def set_avatar(request, username):
    form = ImageForm(request.POST, request.FILES)
    if username != request.user.username:
        return redirect('/')
    if True or form.is_valid():
        image = form.save()
        user = get_object_or_404(User, username=username)
        user.image = image
        user.save()
        image.save()
        return redirect('/users/{}/'.format(username))

    return redirect('/users/{}/edit'.format(username))

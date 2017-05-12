from django.shortcuts import render_to_response
from django.contrib.postgres.search import SearchVector
from django.contrib.auth.models import User
from django_comments.models import Comment
from employees.models import Employee

def employees(request):
    query = request.GET.get('query')
    employees = Employee.objects.annotate(
        search=SearchVector(
            'firstName',
            'lastName',
            'middleName',
            'academicDepartment',
            'description',
            '_memes',
        )).filter(search=query)
    context = {
        'employees': employees,
        'query': query or "",
        'username': request.user.username,
    }
    return render_to_response('search/employees.html', context)

def users(request):
    query = request.GET.get('query')
    users = User.objects.annotate(
        search=SearchVector(
            'username',
            'last_name',
            'first_name',
        )).filter(search=query)
    context = {
        'users': users,
        'query': query or "",
        'username': request.user.username,
    }
    return render_to_response('search/users.html', context)


def comments(request):
    query = request.GET.get('query')
    comments = Comment.objects.annotate(
        search=SearchVector(
            'user_name',
            'comment',
        )).filter(search=query)
    context = {
        'comments': comments,
        'query': query or "",
        'username': request.user.username,
    }
    return render_to_response('search/comments.html', context)

def tags(request):
    query = request.GET.get('query')
    employees = Employee.objects.filter(
        tags__name__in=[query]
    )
    context = {
        'employees': employees,
        'query': query or "",
        'username': request.user.username,
    }
    return render_to_response('search/tags.html', context)

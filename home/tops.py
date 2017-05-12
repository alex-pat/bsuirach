from django.contrib.auth.models import User
from django_comments.models import Comment
from employees.models import Employee

TOP_USERS = None

TOP_EMPLOYEES = None

def update_users():
    global TOP_USERS
    users = [(user, len(user.comment_comments.all()))
             for user in User.objects.all()]
    users.sort(key=lambda x: -x[1])
    TOP_USERS = users[:10]


def update_employees():
    global TOP_EMPLOYEES
    employees = {}
    for comment in Comment.objects.all():
        empl_pk = comment.content_object.pk
        if empl_pk not in employees:
            employees[empl_pk] = 0
        employees[empl_pk] += 1
    empls = [empl_pk for empl_pk, comments in sorted(employees.items(), key=lambda e: e)]
    TOP_EMPLOYEES = [(Employee.objects.get(pk=pk), employees[pk])
                     for pk in empls[:10]]

TOP_USERS = update_users()

TOP_EMPLOYEES = update_employees()

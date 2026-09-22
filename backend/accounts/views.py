from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect


def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            # Admin
            if user.is_superuser or user.is_staff:
                return redirect('admin_dashboard')

            # Teacher
            if user.groups.filter(name='Teacher').exists():
                return redirect('teacher_dashboard')

            # Student
            if user.groups.filter(name='Student').exists():
                return redirect('student_dashboard')

            # No role assigned
            return render(
                request,
                'accounts/login.html',
                {
                    'error': 'No role has been assigned to this account.'
                }
            )

        return render(
            request,
            'accounts/login.html',
            {
                'error': 'Invalid username or password.'
            }
        )

    return render(request, 'accounts/login.html')


@login_required
def admin_dashboard(request):

    if not (request.user.is_superuser or request.user.is_staff):
        return redirect('login')

    return render(
        request,
        'admin/dashboard.html'
    )


@login_required
def teacher_dashboard(request):

    if not request.user.groups.filter(name='Teacher').exists():
        return redirect('login')

    return render(
        request,
        'teacher/dashboard.html'
    )


@login_required
def student_dashboard(request):

    if not request.user.groups.filter(name='Student').exists():
        return redirect('login')

    return render(
        request,
        'student/dashboard.html'
    )
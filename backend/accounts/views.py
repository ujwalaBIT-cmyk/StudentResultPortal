from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from students.models import Student
from classes.models import Class
from subjects.models import Subject
from results.models import Exam, Result


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

    context = {
        'total_students': Student.objects.count(),
        'total_teachers': 0,
        'total_classes': Class.objects.count(),
        'total_subjects': Subject.objects.count(),
        'total_exams': Exam.objects.count(),
        'total_results': Result.objects.count(),
    }

    return render(
        request,
        'admin/dashboard.html',
        context
    )


@login_required
def teacher_dashboard(request):

    if not request.user.groups.filter(name='Teacher').exists():
        return redirect('login')

    context = {
        'total_students': Student.objects.count(),
        'total_classes': Class.objects.count(),
        'total_subjects': Subject.objects.count(),
        'total_exams': Exam.objects.count(),
        'total_results': Result.objects.count(),

        'classes': Class.objects.all(),
        'subjects': Subject.objects.all(),
        'exams': Exam.objects.all(),
    }

    return render(
        request,
        'teacher/dashboard.html',
        context
    )


@login_required
def student_dashboard(request):

    if not request.user.groups.filter(name='Student').exists():
        return redirect('login')

    student = Student.objects.filter(
        user=request.user
    ).first()

    if not student:
        return render(
            request,
            'student/dashboard.html',
            {
                'error': 'No student profile is linked to this account.'
            }
        )

    results = Result.objects.filter(
        student=student
    ).select_related(
        'subject',
        'exam'
    )

    total_marks = sum(
        float(result.marks)
        for result in results
    )

    total_max_marks = sum(
        float(result.max_marks)
        for result in results
    )

    percentage = 0

    if total_max_marks > 0:
        percentage = round(
            (total_marks / total_max_marks) * 100,
            2
        )

    context = {
        'student': student,
        'results': results,
        'total_marks': total_marks,
        'total_max_marks': total_max_marks,
        'percentage': percentage,
    }

    return render(
        request,
        'student/dashboard.html',
        context
    )
    
@login_required
def add_result(request):

    if not request.user.groups.filter(name='Teacher').exists():
        return redirect('login')

    if request.method == 'POST':

        student_id = request.POST.get('student')
        subject_id = request.POST.get('subject')
        exam_id = request.POST.get('exam')
        marks = request.POST.get('marks')
        max_marks = request.POST.get('max_marks')
        remarks = request.POST.get('remarks')

        try:
            marks_value = float(marks)
            max_marks_value = float(max_marks)

            if max_marks_value <= 0:
                raise ValueError

            percentage = (
                marks_value / max_marks_value
            ) * 100

            if percentage >= 90:
                grade = 'A+'
            elif percentage >= 80:
                grade = 'A'
            elif percentage >= 70:
                grade = 'B+'
            elif percentage >= 60:
                grade = 'B'
            elif percentage >= 50:
                grade = 'C'
            elif percentage >= 40:
                grade = 'D'
            else:
                grade = 'F'

            Result.objects.create(
                student_id=student_id,
                subject_id=subject_id,
                exam_id=exam_id,
                marks=marks_value,
                max_marks=max_marks_value,
                grade=grade,
                remarks=remarks
            )

            return redirect('teacher_dashboard')

        except (ValueError, TypeError):

            return render(
                request,
                'teacher/add_result.html',
                {
                    'students': Student.objects.all(),
                    'subjects': Subject.objects.all(),
                    'exams': Exam.objects.all(),
                    'error': 'Please enter valid marks.'
                }
            )

    context = {
        'students': Student.objects.all(),
        'subjects': Subject.objects.all(),
        'exams': Exam.objects.all(),
    }

    return render(
        request,
        'teacher/add_result.html',
        context
    )
    
@login_required
def view_results(request):

    if not request.user.groups.filter(name='Teacher').exists():
        return redirect('login')

    results = Result.objects.select_related(
        'student',
        'subject',
        'exam'
    ).all().order_by(
        '-updated_at'
    )

    context = {
        'results': results,
    }

    return render(
        request,
        'teacher/results.html',
        context
    )
    
@login_required
def update_result(request, result_id):

    if not request.user.groups.filter(name='Teacher').exists():
        return redirect('login')

    try:
        result = Result.objects.get(id=result_id)
    except Result.DoesNotExist:
        return redirect('view_results')

    if request.method == 'POST':

        student_id = request.POST.get('student')
        subject_id = request.POST.get('subject')
        exam_id = request.POST.get('exam')
        marks = request.POST.get('marks')
        max_marks = request.POST.get('max_marks')
        remarks = request.POST.get('remarks')

        try:
            marks_value = float(marks)
            max_marks_value = float(max_marks)

            if max_marks_value <= 0:
                raise ValueError

            if marks_value < 0 or marks_value > max_marks_value:
                raise ValueError

            percentage = (
                marks_value / max_marks_value
            ) * 100

            if percentage >= 90:
                grade = 'A+'
            elif percentage >= 80:
                grade = 'A'
            elif percentage >= 70:
                grade = 'B+'
            elif percentage >= 60:
                grade = 'B'
            elif percentage >= 50:
                grade = 'C'
            elif percentage >= 40:
                grade = 'D'
            else:
                grade = 'F'

            result.student_id = student_id
            result.subject_id = subject_id
            result.exam_id = exam_id
            result.marks = marks_value
            result.max_marks = max_marks_value
            result.grade = grade
            result.remarks = remarks

            result.save()

            return redirect('view_results')

        except (ValueError, TypeError):

            context = {
                'result': result,
                'students': Student.objects.all(),
                'subjects': Subject.objects.all(),
                'exams': Exam.objects.all(),
                'error': 'Please enter valid marks.',
            }

            return render(
                request,
                'teacher/update_result.html',
                context
            )

    context = {
        'result': result,
        'students': Student.objects.all(),
        'subjects': Subject.objects.all(),
        'exams': Exam.objects.all(),
    }

    return render(
        request,
        'teacher/update_result.html',
        context
    )
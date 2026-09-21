from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def student_home(request):
    return JsonResponse({
        "message": "Student Result Portal - Student API",
        "status": "success"
    })
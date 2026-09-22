from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views


urlpatterns = [

    path('login/',views.login_view,name='login'),
    path('logout/',LogoutView.as_view(next_page='/accounts/login/'),name='logout'),
    path('admin-dashboard/',views.admin_dashboard,name='admin_dashboard'),

    path('teacher-dashboard/',views.teacher_dashboard,name='teacher_dashboard'),

    path('student-dashboard/',views.student_dashboard,name='student_dashboard'),
    path('add-result/',views.add_result,name='add_result'),
    path('results/',views.view_results,name='view_results'),
    path('update-result/<int:result_id>/',views.update_result,name='update_result'),
]
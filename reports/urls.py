from django.urls import path

from reports.views import employee_reports, upload_reports

urlpatterns = [
    path('employee_reports', employee_reports, name='employee_reports'),
    path('upload_report', upload_reports, name='upload_report'),
]
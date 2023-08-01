import csv
import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import *

from openpyxl import Workbook
from openpyxl.writer.excel import save_virtual_workbook

from reports.forms import EmployeeReportForm
from django.db import connection

from employees.models import Employee

from tablib import Dataset
from .resources import EmployeeResource

# Create your views here.

@login_required()
def employee_reports(request):
    form = EmployeeReportForm()
    context = {'form': form}
    template_name = 'reports/employee_reports.html'
    
    if request.method == "POST":
        start_date = request.POST.get("emp_start_date")
        end_date = request.POST.get("emp_end_date")
        print(start_date)
        print(end_date)
        start_date = datetime.strptime(str(start_date), "%Y-%m-%d").date()
        end_date = datetime.strptime(str(end_date), "%Y-%m-%d").date()
        end_date = end_date + timedelta(days=1)
        workbook = Workbook()

        employee_id = request.POST.getlist('employee')
        if request.user.user_type == "Admin":
            sheet_no = workbook.active
            task = Employee.objects.filter(join_date__range=[start_date, end_date])
            sheet_no.append([ f"From Date : {start_date}",f"To Date:  {end_date}", ])
            sheet_no.append([])
            sheet_no.append(
                ["Date", "Employee Name", "Created By", "Employee No", "Skills", 	"Phone",  "Address","Department", "Designation", "Location"])
            for i in task:
                second_row = [str(i.emp_start_date), str(i.name),
                                str(i.created_user), str(i.employee_no), str(i.skills), 
                                str(i.phone),str(i.address),str(i.department_name),str(i.designation_name),
                                str(i.location_name)]
                sheet_no.append(second_row)
            response = HttpResponse(content=save_virtual_workbook(workbook),  content_type='vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename=EmployeeReport.xlsx'
            return response
        # else:
        #     sheet_no = workbook.active
        #     task = employee.filter(employee_id__in=employee_id, join_date__range=[start_date, end_date])
        #     sheet_no.append([ f"From Date : {start_date}",f"To Date:  {end_date}"])
        #     sheet_no.append([])
        #     sheet_no.append(
        #         ["Date", "Employee Name", "Created By", "Employee No", "Skills", 	"Phone",  "Address","Department", "Designation", "Location"])
        #     for i in task:
        #         second_row = [str(i.emp_start_date), str(i.name),
        #                         str(i.created_user), str(i.employee_no), str(i.skills), 
        #                         str(i.phone),str(i.address),str(i.department_name),str(i.designation_name),
        #                         str(i.location_name)]
        #         sheet_no.append(second_row)
        #     response = HttpResponse(content=save_virtual_workbook(workbook),  content_type='vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        #     response['Content-Disposition'] = 'attachment; filename=EmployeeReport.xlsx'
        #     return response
    return render(request,template_name, context)



def upload_reports(request):
    if request.method =='POST':
        employee_resource = EmployeeResource()
        dataset = Dataset()
        new_employee = request.FILES['my_file']
        imported_data = dataset.load(new_employee.read(), format='xlsx')
        for data in imported_data:
            value = Employee(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
                data[6],
                data[7],
                data[8],
                data[9],
                data[10],
                data[11]
                
            )
            value.save()

    return render(request, 'reports/upload_report.html')
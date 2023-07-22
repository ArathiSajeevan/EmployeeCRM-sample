import csv
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from reports.forms import EmployeeReportForm
from django.db import connection

# Create your views here.

@login_required
def employee_reports(request):
    form = EmployeeReportForm()
    context = {'form': form}
    template_name = 'reports/employee_reports.html'
    if request.method == "POST":
        
        employee = request.POST.get('employee')
        print("employee", employee)

        script = """ SELECT em.name, em.employee_no, em.skills, em.join_date, em.emp_start_date, em.emp_end_date, 
                                    em.phone, em.address, em.image, dp.department_name, dg.designation_name, lc.location_name
                                    FROM employee_crm_db.employees_employee em
                                    left join employee_crm_db.master_tbl_department dp on em.department_name_id=dp.department_id
                                    left join employee_crm_db.master_designation dg on em.designation_name_id=dg.designation_id
                                    left join employee_crm_db.master_location lc on em.location_name_id=lc.location_id"""
        if employee == '':
            script = script

        else:
            employee = employee.replace("-", "")
            script += """ where em.employee_id='{}' """
            script = script.format(employee)

        with connection.cursor() as cursor:
            cursor.execute(script)
            task = cursor.fetchall()

        response = HttpResponse(content_type='ms-excel')
        file_name = "Employee Report.csv"
        response['Content-Disposition'] = 'attachment; filename = "' + file_name + '"'
        writer = csv.writer(response)

        writer.writerow([""])
        first_row = ["Employee Name", "Employee No", "Skills", "Join Date", "Employee Start Date", "Employee End Date",
                     "Phone", "Address", "Image", "Department", "Designation", "Location"]
        writer.writerow(first_row)
        writer.writerow([""])
        for i in task:
            second_row = [i[0], i[1], i[2], i[3], i[4], i[5], 
                          i[6], i[7], i[8], i[9], i[10]]
            writer.writerow(second_row)
        return response
    return render(request, template_name, context)
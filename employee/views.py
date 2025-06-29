from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from .models import Employee
from .forms import EmployeeForm

# List view – Display, filter, and paginate employees
def employee_list(request):
    query = request.GET.get("q", "")
    employees = Employee.objects.all().order_by("id")
    if query:
        employees = employees.filter(name_of_employee__icontains=query)
    paginator = Paginator(employees, 10)
    page_number = request.GET.get("page")
    try:
        employees_page = paginator.get_page(page_number)
    except (PageNotAnInteger, EmptyPage):
        employees_page = paginator.get_page(1)
    return render(request, "employee/employee_list.html", {
        "employees": employees_page,
        "query": query
    })

# Create & Update view – Handle employee form submissions
def employee_form(request, id=None):
    employee = get_object_or_404(Employee, id=id) if id else None
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, "Employee saved successfully.")
            return redirect("employee_list")
    else:
        form = EmployeeForm(instance=employee)
    return render(request, "employee/employee_form.html", {"form": form})

# Delete view – Remove an employee entry
def employee_delete(request, id):
    employee = get_object_or_404(Employee, id=id)
    employee.delete()
    messages.warning(request, f"Employee '{employee.name_of_employee}' deleted.")
    return redirect("employee_list")


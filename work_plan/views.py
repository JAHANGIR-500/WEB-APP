from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.http import JsonResponse
from .models import WorkPlan
from .forms import WorkPlanForm

# 📋 List view – Display, filter, and paginate work plans
def work_plan_list(request):
    query = request.GET.get("q", "")
    work_plans = WorkPlan.objects.select_related("project", "task").order_by("id")

    if query:
        work_plans = work_plans.filter(project__name_of_project__icontains=query)

    paginator = Paginator(work_plans, 10)
    page_number = request.GET.get("page")
    try:
        work_plan_page = paginator.get_page(page_number)
    except (PageNotAnInteger, EmptyPage):
        work_plan_page = paginator.get_page(1)

    return render(request, "work_plan/work_plan_list.html", {
        "work_plan": work_plan_page,
        "query": query
    })

# ✏️ Create & Update view – Handle work plan form submissions
def work_plan_form(request, id=None):
    work_plan = get_object_or_404(WorkPlan, id=id) if id else None
    if request.method == "POST":
        form = WorkPlanForm(request.POST, instance=work_plan)
        if form.is_valid():
            saved_plan = form.save()
            action = "updated" if id else "created"
            messages.success(request, f"Work plan for '{saved_plan.project.name_of_project}' {action}.")
            return redirect("work_plan_list")
    else:
        form = WorkPlanForm(instance=work_plan)

    return render(request, "work_plan/work_plan_form.html", {"form": form})

# ❌ Delete view – Remove a work plan entry
def work_plan_delete(request, id):
    try:
        work_plan = WorkPlan.objects.get(id=id)
        project_name = work_plan.project.name_of_project
        work_plan.delete()
        messages.warning(request, f"Work plan for '{project_name}' deleted.")
    except WorkPlan.DoesNotExist:
        messages.error(request, "Work plan not found.")
    return redirect("work_plan_list")

# 📈 Gantt chart data – Provide JSON data for frontend chart
def gantt_chart_data(request):
    work_plans = WorkPlan.objects.filter(
        start_date__isnull=False,
        finish_date__isnull=False
    ).select_related("task").order_by("start_date")

    data = []
    for plan in work_plans:
        if plan.start_date and plan.finish_date:
            data.append({
                "id": str(plan.id),
                "name": plan.task.name_of_task,
                "start": plan.start_date.strftime('%Y-%m-%d'),
                "end": plan.finish_date.strftime('%Y-%m-%d'),
                "progress": plan.progress or 0,
            })

    return JsonResponse(data, safe=False)






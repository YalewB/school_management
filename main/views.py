from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Student, Teacher, Admin, Director, Parent, Finance, Course, Grade, Enrollment  # Import Enrollment

@login_required
def student_dashboard(request):
    student = Student.objects.get(user=request.user)  # Get the student instance
    context = {
        'student': student,
    }
    return render(request, 'student_dashboard.html', context)

@login_required
def teacher_dashboard(request):
    teacher = Teacher.objects.get(user=request.user)  # Get the teacher instance
    context = {
        'teacher': teacher,
    }
    return render(request, 'teacher_dashboard.html', context)

@login_required
def admin_dashboard(request):
    admin = Admin.objects.get(user=request.user)  # Get the admin instance
    # Example stats, replace with actual logic
    total_students = Student.objects.count()
    total_teachers = Teacher.objects.count()
    total_courses = Course.objects.count()
    recent_activities = []  # Fetch recent activities as per your logic

    context = {
        'admin': admin,
        'total_students': total_students,
        'total_teachers': total_teachers,
        'total_courses': total_courses,
        'recent_activities': recent_activities,
    }
    return render(request, 'admin_dashboard.html', context)

@login_required
def director_dashboard(request):
    director = Director.objects.get(user=request.user)  # Get the director instance
    total_enrollments = Enrollment.objects.count()  # Now this line should work
    active_teachers = Teacher.objects.filter(classes__isnull=False).count()  # Count active teachers

    context = {
        'director': director,
        'total_enrollments': total_enrollments,
        'active_teachers': active_teachers,
    }
    return render(request, 'director_dashboard.html', context)

@login_required
def parent_dashboard(request):
    parent = Parent.objects.get(user=request.user)  # Get the parent instance
    children = parent.children.all()  # Get all children associated with the parent
    events = []  # Fetch events relevant to the parent

    context = {
        'parent': parent,
        'children': children,
        'events': events,
    }
    return render(request, 'parent_dashboard.html', context)

@login_required
def finance_dashboard(request):
    finance_data = Finance.objects.all()  # Fetch all financial records
    total_revenue = sum(transaction.amount for transaction in finance_data if transaction.transaction_type == 'income')
    total_expenses = sum(transaction.amount for transaction in finance_data if transaction.transaction_type == 'expense')
    net_profit = total_revenue - total_expenses

    context = {
        'total_revenue': total_revenue,
        'total_expenses': total_expenses,
        'net_profit': net_profit,
        'transactions': finance_data,
    }
    return render(request, 'finance_dashboard.html', context)
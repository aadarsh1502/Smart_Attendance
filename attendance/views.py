from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Faculty, Student, Subject, Attendance
from django.utils import timezone

@login_required
def dashboard(request):
    user = request.user

    if user.is_superuser:
        return redirect('/admin/')

    if Faculty.objects.filter(user=user).exists():
        faculty = Faculty.objects.get(user=user)
        subjects = Subject.objects.filter(faculty=faculty)
        return render(request, 'faculty_dashboard.html', {'subjects': subjects})

    if Student.objects.filter(user=user).exists():
        student = Student.objects.get(user=user)
        subjects = Subject.objects.all()

        subject_data = []
        total_present = 0
        total_classes = 0

        for subject in subjects:
            records = Attendance.objects.filter(student=student, subject=subject)

            subject_total = records.count()
            subject_present = records.filter(status="Present").count()

            percentage = 0
            if subject_total > 0:
                percentage = (subject_present / subject_total) * 100

            subject_data.append({
                'name': subject.name,
                'percentage': round(percentage, 2),
                'present': subject_present,
                'total': subject_total
            })

            total_present += subject_present
            total_classes += subject_total

        overall_percentage = 0
        if total_classes > 0:
            overall_percentage = (total_present / total_classes) * 100

        context = {
            'subject_data': subject_data,
            'overall_percentage': round(overall_percentage, 2),
            'total_present': total_present,
            'total_classes': total_classes
        }

        return render(request, 'student_dashboard.html', context)

    return render(request, 'no_role.html')


from django.utils import timezone

@login_required
def mark_attendance(request, subject_id):
    subject = Subject.objects.get(id=subject_id)
    students = Student.objects.all().order_by('roll_number')

    if request.method == "POST":
        present_students = request.POST.getlist('students')
        present_students = list(map(int, present_students))

        faculty = Faculty.objects.get(user=request.user)
        today = timezone.now().date()

        for student in students:
            if student.id in present_students:
                status = "Present"
            else:
                status = "Absent"

            Attendance.objects.update_or_create(
                student=student,
                subject=subject,
                date=today,
                defaults={
                    'status': status,
                    'marked_by': faculty
                }
            )

        return redirect('dashboard')

    return render(request, 'mark_attendance.html', {
        'subject': subject,
        'students': students
    })
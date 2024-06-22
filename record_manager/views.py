from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student


def student_info(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/records')
            except Exception:
                pass
        else:
            form = StudentForm()
        return render(request, 'index.html', {'form':form})

def records(request):
    students = Student.objects.all()
    return render(request, 'records.html', {'students':students})

def edit_record(request, id):
    student = Student.objects.get(id=id)
    return render(request, 'edit_record.html', {'student':student})

def update_record(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(request.POST, instance=student)
    if form.is_valid():
        form.save()
        return redirect('/records')
    return render(request, 'edit_record.html', {'student':student})

def del_record(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('/records')

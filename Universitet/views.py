from django.shortcuts import render

from . import models

def main(request):
    faculty = models.Faculty.objects.all()
    ctx = {'faculties': faculty}
    return render(request, 'Faculty.html', ctx)

def kafedra(request, pk):
    kafedralar = models.Faculty.objects.get(pk=pk)
    cxt = {'faculty': kafedralar}
    return render(request, 'Kafedra.html', cxt)

def group(request, pk):
    groups = models.Kafedra.objects.get(pk=pk)
    cxt = {'groups': groups}
    return render(request, 'Group.html', cxt)

def student(request, pk):
    students = models.Group.objects.get(pk=pk)
    cxt = {'students': students}
    return render(request, 'Student.html', cxt)

def student_details(request, pk):
    students = models.Student.objects.get(pk=pk)
    cxt = {'students': students}
    return render(request, 'Student details.html', cxt)


def subject(request):
    subjects = models.Subject.objects.all()
    cxt = {'subjects': subjects}
    return render(request, 'Subject.html', cxt)

def teacher(request, pk):
    teachers = models.Teacher.objects.get(pk=pk)
    cxt = {'teachers': teachers}
    return render(request, 'Teacher.html', cxt)

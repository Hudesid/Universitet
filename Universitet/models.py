from django.db import models

class Faculty(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Kafedra(models.Model):
    name = models.CharField(max_length=100)
    faculty = models.ForeignKey(Faculty, related_name='kafedra', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Kafedra, related_name='groups', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, default='Unknown')
    group = models.ForeignKey(Group, related_name='students', on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name

class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, default="Unknown")
    subject = models.ForeignKey(Subject, related_name='teachers', on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name

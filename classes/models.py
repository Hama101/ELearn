from django.db import models
from users.models import Profile

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    surname = models.CharField(max_length=50, blank=True, null=True)

    email = models.EmailField( blank=True, null=True)
    age = models.IntegerField( blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_of_birth = models.DateField( blank=True, null=True)
    
    is_present   = models.BooleanField( blank=True, null=True , default=True)
    situation = models.CharField(max_length=50, blank=True, null=True)
    

    photo = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.name +" "+self.surname



class Group(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    year = models.IntegerField( blank=True, null=True)
    students = models.ManyToManyField(Student, blank=True, null=True)
    mail = models.EmailField( blank=True, null=True)

    @property
    def students_number(self):
        return self.students.count()


    def __str__(self):
        return self.name


class Teacher(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, blank=True, null=True)
    mail_pro = models.EmailField( blank=True, null=True)

    @property
    def get_image(self):
        return self.profile.profile_image.url
    
    def __str__(self):
        return self.profile.user.username


class Subject(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    nbr_heurs = models.IntegerField( blank=True, null=True)
    _type = models.CharField(max_length=50, blank=True, null=True)
    level = models.IntegerField( blank=True, null=True)
    
    def __str__(self):
        return self.name

class Seance(models.Model):
    start_hour = models.TimeField( blank=True, null=True)
    end_hour = models.TimeField( blank=True, null=True)
    date = models.DateField( auto_now_add=False, blank=True, null=True)
    salle_number = models.IntegerField( blank=True, null=True)
    objective = models.CharField(max_length=50, blank=True, null=True)
    tools = models.CharField(max_length=50, blank=True, null=True)

    group = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, blank=True, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.subject.name}-->{self.objective}-->{self.group}"


class Absent(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, null=True)
    seance = models.ForeignKey(Seance, on_delete=models.CASCADE, blank=True, null=True)
    
    date = models.DateTimeField(null=True, blank=True,auto_now_add=True)

    def __str__(self):
        return f"{self.student.name} : {self.seance}"


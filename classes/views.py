from django.shortcuts import render
from .models import *
from datetime import date
from django.http import JsonResponse


# Create your views here.

def seances(request):
    today = date.today()
    seances = Seance.objects.filter(date=today).order_by('start_hour')
    context = {
        'seances': seances,
    }
    return render(request, 'seances.html' , context)


def seance_detail(request, pk):
    seance = Seance.objects.get(pk=pk)
    context = {
        'seance': seance,
    }
    return render(request, 'seance_detail.html', context)


def set_student_present(request):
    pk = request.GET.get('pk')
    student = Student.objects.get(pk=pk)
    student.is_present = True
    student.save()
    return JsonResponse({'status': 'ok'})



def set_student_absent(request):
    pk1 , pk2 = request.GET.get('pk').split('-')
    student = Student.objects.get(pk=pk1)
    seance = Seance.objects.get(pk=pk2)
    
    student.is_present = False
    student.save()
    
    absent = Absent()
    absent.student = student
    absent.seance = seance
    absent.save()
    
    return JsonResponse({'status': 'ok'})
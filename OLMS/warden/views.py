from django.shortcuts import render
from student.models import Leave,Outing

def showAllLeaves(request):
    leaves = Leave.objects.all()
    return render(request,'showAllLeaves.html',{"leaves":leaves})

def showAllOutings(request):
    outings = Outing.objects.all()
    return render(request,'showAllOutings.html',{"outings":outings})
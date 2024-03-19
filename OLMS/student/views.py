from django.shortcuts import render,redirect
from student.models import Leave,Outing
from django.contrib.auth import get_user_model
customUser=get_user_model()
def leaveForm(request):
    if request.method == "POST":
        user = request.user
        start_date = request.POST['outdate']
        end_date = request.POST['indate']
        reason = request.POST['reason']
        obj = Leave.objects.create(user=user,start_date=start_date,end_date=end_date,reason=reason)
        obj.save()
        return redirect('show-leaves')
    return render(request,'leave_application_form.html')

def getUser(id):
    return customUser.objects.get(id=id)
def showLeaves(request):
    id= request.user.id
    user =getUser(id)
    leaves = Leave.objects.filter(user=user)
    leaves_details = []
    for leave in leaves:
        leave_dict = {
            'start_date': leave.start_date,
            'end_date': leave.end_date,
            'reason': leave.reason
        }
        leaves_details.append(leave_dict)
    return render(request,'showLeaves.html',{'leaves':leaves})

def showOutings(request):
    id= request.user.id
    user =getUser(id)
    outings = Outing.objects.filter(user=user)
    outing_details = []
    for outing in outings:
        outing_dict = {
            'in_time': outing.in_time,
            'out_time': outing.out_time,
            'reason':outing.reason
        }
        outing_details.append(outing_dict)
        print(outing_details)
    return render(request,'showOutings.html',{'outings':outings})

def OutingForm(request):
    if request.method == "POST":
        user = request.user
        out_time= request.POST['outtime']
        in_time = request.POST['intime']
        reason = request.POST['reason']
        obj = Outing.objects.create(user=user,in_time=in_time,out_time=out_time,reason=reason)
        obj.save()
        return redirect('show-outings')
    return render(request,'outing_application_form.html')


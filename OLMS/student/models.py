from django.db import models
from django.contrib.auth import get_user_model

student = get_user_model()

class Leave(models.Model):
    user = models.ForeignKey(student,on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    # num = models.IntegerField()
    # record_out_time = models.DateTimeField(auto_now_add=True)
    # record_in_time = models.DateField(auto)
   


class Outing(models.Model):
    user = models.ForeignKey(student,on_delete=models.CASCADE)
    out_time = models.TimeField()
    in_time = models.TimeField()
    date = models.DateField(auto_now_add=True)
    reason = models.TextField()
    # num = models.IntegerField()

   
from django.db import models
from django.contrib.auth.models import AbstractUser
ROLE_CHOICE =[
    ('warden',"Warden"),
    ('security',"Security"),
    ('student',"Student")
    ]
class CustomUser(AbstractUser):
    email = models.EmailField()
    role = models.CharField(max_length=50,choices=ROLE_CHOICE)
   
    def __str__(self):
        return self.email 
    

    
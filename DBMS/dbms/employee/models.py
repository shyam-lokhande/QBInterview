from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class File(models.Model):
    file=models.FileField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    APPROVAL_CHOICES=(
        ('A','Approved'),
        ('R','Rejected'),
        ('P','Pending')

    )
    approval_status=models.CharField(max_length=1,choices=APPROVAL_CHOICES,default='P')

    

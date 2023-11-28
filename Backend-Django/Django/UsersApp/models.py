from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

# Create your models here.
class User (models.Model):
    user_id = models.BigAutoField(primary_key=True)
    email = models.CharField(max_length=200, validators=[validate_email], default='email',unique=True)
    firstname = models.CharField( max_length=100, default='firstname')
    lastname = models.CharField( max_length=100, default='lastname')    
    password = models.CharField(max_length=200, default='pwd')

class Logs(models.Model):
    log_id = models.BigAutoField( primary_key=True)
    user_id =  models.ForeignKey(User, on_delete=models.CASCADE, default = 1)
    log_in_time =  models.DateTimeField(null=True) 
    log_out_time =  models.DateTimeField(null=True) 

class Pages(models.Model):
    page_visit_id = models.BigAutoField( primary_key=True)
    user_id =  models.ForeignKey(User, on_delete=models.CASCADE, default = 1)
    log_id =  models.ForeignKey(Logs, on_delete=models.CASCADE,default = 1)
    page_name = models.CharField( max_length=100, default='PageName')
    start_time =  models.DateTimeField(null=True) 
    end_time =  models.DateTimeField(null=True) 
    time_spent = models.DateTimeField(null=True)


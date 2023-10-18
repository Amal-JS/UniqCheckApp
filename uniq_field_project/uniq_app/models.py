from django.db import models
from django.forms import ValidationError

# Create your models here.

class CustomUser(models.Model):

    def username_check(value):
        if not value[0].isupper():
            raise ValidationError("Username first letter must be capital")
        if len(value)<5:
            raise ValidationError("Username atleast 5 characters")
        if CustomUser.objects.filter(username=value).exists():
            raise ValidationError("Username already exists")
        return value
    
    def email_check(value):
        if '@' not in value or '.' not in value:
            raise ValidationError("Enter valid Email")
        
        if CustomUser.objects.filter(username=value).exists():
            raise ValidationError("Email already exists")
        return value
    
    def phone_number_check(value):
        
        if len(str(value))<5:
            raise ValidationError("Phone Number must have 10 numbers")
        
        if CustomUser.objects.filter(username=value).exists():
            raise ValidationError("Phone Number already exists")
        return value
    

    username = models.CharField(max_length=30,unique=True,validators=[username_check])
    email = models.EmailField(unique=True,validators=[email_check])
    phone = models.IntegerField(unique=True,validators=[phone_number_check])

    def __str__(self):
        return self.username
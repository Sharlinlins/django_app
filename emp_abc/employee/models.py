from django.db import models
from django.core import validators as v


# Create your models here.
class Employee(models.Model):
    ROLE = (
        ('Senior Developer', 'Senior Developer'),
        ('Junior Developer', 'Junior Developer'),
        ('Software Tester', 'Software Tester')
    )
    
    def __str__(self):
        return self.name

    name = models.CharField(
        max_length = 50,
        verbose_name = 'NAME',
        validators =[
            v.MinLengthValidator(3, 'Name should be 3 chars long'),
            v.MaxLengthValidator(50, 'Name shoild not be longer than 50 chars')
        ]
    )
    email = models.CharField(
        max_length = 50,
        verbose_name = 'EMAIL',
        unique = True,
        validators =[
            v.MinLengthValidator(5, 'Name should be 5 chars long'),
            v.MaxLengthValidator(50, 'Name shoild not be longer than 50 chars'),
            v.EmailValidator("Invalid Email")
        ]
    )
    age = models.IntegerField(
        verbose_name = 'AGE',
        validators =[
            v.MinValueValidator(20, 'Age should be above 20'),
            v.MaxValueValidator(70, 'Age should be below 70'),
        ]
    )
    phone = models.BigIntegerField(
        verbose_name = 'PHONE',
        default = 0,
        unique = True,
        validators =[
            v.MinValueValidator(6666666666, 'Invalid Phone Number'),
            v.MaxValueValidator(9999999999, 'Invalid Phone Number'),
        ]
    )
    role = models.CharField(
        max_length = 100,
        verbose_name = 'ROLE',
        choices = ROLE
    )
    address = models.CharField(
        max_length = 255,
        verbose_name = 'ADDRESS',
        default = 0
    )
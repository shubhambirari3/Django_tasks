from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)


def _str_(self):
    return self.name



# from app2.models import User

# User.objects.create(name='John',email = "john@mail.comm",password = "123456",phone = "1234567890")
# User.objects.create(name='Doe',email = "doe@mail.comm",password = "123456",phone = "1234567890")

# User.objects.all()
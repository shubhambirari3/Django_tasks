from django.db import models


class PersonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    bio = models.TextField()
    adress = models.TextField(max_length=100 , default='' , blank=True)
    email = models.EmailField(max_length=100 , default='' , blank=True)
    phone = models.CharField(max_length=15 , default='' , blank=True)

    def __str__(self):
        return self.name



# python manage.py makemigrations
# python manage.py migrate
# python manage.py showmigrations       # to show all migrations
# python manage.py migrate app1 zero          # to remove all migrations
# python manage.py migrate app1 0001_initial     # to migrate to a specific migration


# powershell Terminal Command:
# python manage.py shell

# Testing in Shell for PersonInfo:

# from app1.models import PersonInfo
# PersonInfo.objects.create(name="Alice", age=30, bio="Software Engineer")
# PersonInfo.objects.create(name="Bob", age=25, bio="Designer")

# print(PersonInfo.objects.all())

#now we can see the data in the database

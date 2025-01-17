from django.db import models


class Attendance(models.Model):
    date = models.DateField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    #profile = models.ForeignKey('app1.Profile', on_delete=models.CASCADE)

    def __str__(self):
        return f"Attendance on {self.date}"
    



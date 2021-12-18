from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date
# Create your models here.
class Health(models.Model):
    patient=models.ForeignKey(User,on_delete=models.CASCADE)
    o2_level=models.IntegerField()
    bp_level=models.IntegerField()
    sugar_level=models.IntegerField()
    crp=models.DecimalField(decimal_places=2,max_digits=2,default=0)
    Feedback=models.TextField()
    report_date=models.DateField(default=date.today)


    def __str__(self):
        return f"{self.patient}"

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('home')
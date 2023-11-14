from django.db import models
from django.utils.translation import gettext_lazy as _

SITUATION=(
    ('Pending','Pending'),
    ('Approved','Approved'),
    ('Disapproved','Disapproved'),
)


class Incident(models.Model):

    name = models.CharField(max_length=100)
    Witnesses = models.CharField(max_length=100)
    Departments = models.CharField(max_length=50)
    Location_Area = models.CharField(max_length=50)
    Incident_report_date = models.DateTimeField(auto_now_add=True)

    Type_of_near_miss = models.CharField(max_length =30)

    Description = models.TextField(max_length=500)

    Safety_violated = models.CharField(max_length =3)

    Recommendation_step = models.TextField(max_length=500)

    situation =models.CharField(max_length=50, null=True,choices=SITUATION,default='Pending')

    def __str__(self):
        return self.name



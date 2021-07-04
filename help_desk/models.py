from django.db import models
from django.db.models.base import ModelStateFieldsCacheDescriptor
from django.db.models.deletion import CASCADE
from registry.models import Customer

# Create your models here.





class Ticket(models.Model):

    customer = models.ForeignKey(Customer, related_name="tickets", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    open_timestamp = models.DateTimeField()
    closed_timestamp = models.DateTimeField()
    issuetext = models.CharField(max_length=1000)
    ticket_state = models.IntegerField()


    def __str__(self):
        return self.title



class Activity(models.Model):
    ticket = models.ForeignKey(Ticket, related_name="activities", on_delete=CASCADE)
    customer = models.ForeignKey(Customer, related_name="activities", on_delete=CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    expected_date = models.DateField()
    expected_time = models.TimeField()
    effective_date = models.DateField(blank=True)
    effective_time = models.TimeField(blank=True)
    activity_state = models.IntegerField(blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        #verbose_name = 'My image'
        verbose_name_plural = 'Activities'
    






    





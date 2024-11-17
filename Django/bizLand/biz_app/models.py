from django.db import models

# Create your models here.


class Company(models.Model):
    """creates common values of all the companies
    - clients
    - project
    - HoursOfSupport
    - workers
    """

    clients = models.IntegerField()
    project = models.IntegerField()
    hoursOfSupport = models.IntegerField()
    workers = models.IntegerField()

 
    def __str__(self):
        return f"company {self.id}"


class Team(models.Model):
    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    profile = models.ImageField(upload_to='profiles')

    def __str__(self):
        return f"{self.full_name}"
    
     
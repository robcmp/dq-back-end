from django.db import models

# Create your models here.


class Client(models.Model):
    objects = models.Manager
    id = models.AutoField(primary_key=True)
    nin = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)

    def __str__(self):
        return self.id


class Company(models.Model):
    objects = models.Manager
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)

    def __str__(self):
        return f'Company ({self.name})'


class Rent(models.Model):
    objects = models.Manager
    id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    daily_cost = models.IntegerField()
    days = models.IntegerField()

    def __str__(self):
        return f'Rent ({self.daily_cost}, {self.days})'

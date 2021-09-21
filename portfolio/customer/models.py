from django.db import models

# Create your models here.

class Transaction(models.Model):
    sender = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    goods = models.CharField(max_length=30)
    gtype = models.CharField(max_length=30)
    price = models.IntegerField()
    fee = models.IntegerField()
    method = models.CharField(max_length=30)
    receiver = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    date = models.DateTimeField()
    branch = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.method + " : " + self.sender 

class Feedback(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    desc = models.TextField()

    def __str__(self):
        return self.name +" - " + self.email

class Transactions(models.Model):
    address = models.CharField(max_length=50)
    date = models.CharField(max_length=50)

    def __str__(self):
        return self.address
    

class Payment(models.Model):
    confirmation = models.CharField(max_length=50)

    def __str__(self):
        return self.confirmation
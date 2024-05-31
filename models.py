from django.db import models

# Create your models here.
class Contact(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Subject = models.CharField(max_length=100)
    Message = models.TextField()

    class Meta:
        db_table = "contact"

class Customer(models.Model):
    email = models.CharField(max_length=100, primary_key=True)
    password = models.CharField(max_length=100)
    mobile = models.BigIntegerField()
    city = models.CharField(max_length=100)

    class Meta:
        db_table = "customer"

class Admin(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = "admin"


class Category(models.Model):
    category = models.CharField(max_length=100)
    class Meta:
        db_table ="category"

class Surveys(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    status = models.IntegerField(default=0)
    class Meta:
        db_table = "Survey"

class Votes(models.Model):
    surveys = models.ForeignKey(Surveys, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField()

    class Meta:
        db_table = "votes"

class Add(models.Model):
    surveys = models.ForeignKey(Surveys, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    class Meta:
        db_table = "add"

class View_options(models.Model):
    surveys = models.ForeignKey(Surveys, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    class Meta:
        db_table = "View_options"

class Add_Election(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    termsandcondition = models.CharField(max_length=100)
    createdate = models.DateField(auto_now_add=True)
    electiondate = models.DateField()
    resultdate = models.DateField()


class Nomination(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    age = models.BigIntegerField()
    qualification = models.CharField(max_length=100)
    about = models.CharField(max_length=100)
    image = models.ImageField()
    idproof = models.ImageField()
    address = models.CharField(max_length=100)
    mobile = models.BigIntegerField()
    email = models.ForeignKey(Customer, on_delete=models.CASCADE)
    election = models.ForeignKey(Add_Election, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, default="pending")


class View_Nomination(models.Model):
    election = models.ForeignKey(Add_Election, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
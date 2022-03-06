from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=20,default=0)
    semester = models.IntegerField(default=0)
    roll_no = models.IntegerField(default=0)
    address = models.CharField(max_length=20, default=0)
    contact = models.IntegerField(default=0)

    def __str__(self):
        return self.name
        
class teacher(models.Model):
    t_name = models.CharField(max_length=20,default=0)
    t_salary=models.IntegerField()

class author(models.Model):
    name = models.CharField(max_length=20,default=0)
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class book(models.Model):
    name = models.CharField(max_length=20)
    no_page = models.IntegerField()
    author = models.ForeignKey(author, on_delete=models.CASCADE)
    price = models.IntegerField()    

    def __str__(self):
        return self.name

class AuthorPenName(models.Model):
    name = models.CharField(max_length=20)
    author = models.OneToOneField(author, on_delete=models.CASCADE)


class Tstudent(models.Model):
    name = models.CharField(max_length=20)
    roll_no = models.IntegerField()
    booked = models.ManyToManyField(book)
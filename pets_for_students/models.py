from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    num_of_cats = models.IntegerField(default=0, editable=False)
    # made uneditable to avoid human errors in the database

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Cat(models.Model):
    name = models.CharField(max_length=128)
    owner = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



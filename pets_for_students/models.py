from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    num_of_cats = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Cat(models.Model):
    name = models.CharField(max_length=128)
    owner = models.ForeignKey(Student, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.update_student_num_of_cats()

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        self.update_student_num_of_cats()

    def update_student_num_of_cats(self):
        owner = self.owner
        owner.num_of_cats = owner.cat_set.count()
        owner.save()

    def __str__(self):
        return self.name



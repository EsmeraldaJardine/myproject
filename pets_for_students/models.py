from django.db import models

class Student(models.Model):
    # any variables go here e.g. NAME_MAX_LENGTH = 128
    # -----
    # input fields here
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    num_of_cats = models.IntegerField(default=0)
 
    # one to one? **REMEMBER** to set model for linked db
    # car = models.OneToOneField(Car, on_delete=models.CASCADE)
    # Foreign key? **REMEMBER** to set model for foreign key argument
    #occupation = models.ForeignKey(Occupation, on_delete=models.CASCADE)

    ## Overwrite save???
    # def save(self, *args, **kwargs):
    #   self.slug = slugify(self.name)
    #   super(Model
    #Name, self).save(*args, **kwargs)
    #
    ## Custom plural? Edit 'PluralName' as appropriate
    # class Meta:
    #   verbose_name_plural = 'PluralName'
    #
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Student(models.Model):
    name = models.CharField(max_length=128)
    owner = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



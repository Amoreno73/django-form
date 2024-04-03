from django.db import models

# So Models inherits from the model class from django.db

class Form(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField()
    date = models.DateField()
    occupation = models.CharField(max_length=80)
    # __str__ creates  a string sentence out of certain variables. 
    # So this magic method determines what will be printed out .
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


#everytime you make changes to db
    # use python manage.py makemigrations
    # the form code is translated into python code

    
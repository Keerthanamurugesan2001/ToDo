from django.db import models


# Create your models here.

class ToDoL(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Items(models.Model):
    todolist = models.ForeignKey(ToDoL, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text

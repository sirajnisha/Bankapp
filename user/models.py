from django.db import models

class District(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Branch(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=100)
    dob= models.DateField(null=True, blank=True)
    age=models.IntegerField()

    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
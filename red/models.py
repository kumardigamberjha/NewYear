from django.db import models

# Create your models here.


class FormModel(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    adult = models.IntegerField()
    child = models.IntegerField()
    img = models.FileField(blank=True, null=True)
    # qrcode = models.CharField(max_length=300)
    invite_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class SaveImage(models.Model):
    img = models.ImageField()

    
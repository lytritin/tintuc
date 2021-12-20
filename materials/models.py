
from django.db import models


class Material(models.Model):
    phieunhap = models.CharField(max_length=1000)
    sohoadon = models.CharField(max_length=100)
    ngaythang = models.DateTimeField()
    tenvattu = models.TextField()

    def __str__(self):
        return self.phieunhap
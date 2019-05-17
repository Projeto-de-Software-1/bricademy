from django.db import models
from django.contrib.auth.models import User


class Address(models.Model):
    CEP = models.CharField('CEP', max_length=15)
    city = models.CharField('Cidade', max_length=50)
    district = models.CharField('Bairro', max_length=30)
    street = models.CharField('Rua', max_length=140)
    number = models.CharField('Numero', max_length=8)
    complement = models.CharField('Complemento', max_length=100)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.street + ', ' + self.number + ', ' + self.district + ' - ' + self.city

from django.db import models


class Categories(models.Model):
    category_name = models.CharField('Categoria', max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.category_name


class Conservations(models.Model):
    CONSERVATION_CHOICES = [
        ('NOVO', 0),
        ('SEMINOVO', 1),
        ('USADO', 2),
        ('MUITO USADO', 3)
    ]
    conservation = models.IntegerField(choices=CONSERVATION_CHOICES)

    def __str__(self):
        return self.conservation


class Material(models.Model):
    title = models.CharField('Título', max_length=50)
    author = models.CharField('Autor', max_length=50)
    ISBN = models.CharField('ISBN', max_length=13)
    publishing_company = models.CharField('Editora', max_length=50)
    publication_date = models.DateField()
    # falta

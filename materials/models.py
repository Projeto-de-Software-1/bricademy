from django.db import models
from django.contrib.auth.models import User


class Subject(models.Model):
    subject = models.CharField('Assunto', max_length=100)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Modificado em', auto_now=True)

    def __str__(self):
        return self.subject


class Material(models.Model):
    CONSERVATION_CHOICES = [
        (0, 'NOVO'),
        (1, 'SEMINOVO'),
        (2, 'USADO'),
        (3, 'MUITO USADO')
    ]
    CATEGORY_CHOICES = [
        (0, 'LIVRO'),
        (1, 'TESE'),
        (2, 'REVISTA'),
        (3, 'ARTIGO'),
        (4, 'RESUMO'),
        (5, 'OUTRO')
    ]
    title = models.CharField('Título', max_length=50)
    author = models.CharField('Autor', max_length=50)
    ISBN = models.CharField('ISBN', max_length=13, blank=True, null=True)
    publishing_company = models.CharField(
        'Editora', max_length=50, blank=True, null=True)
    publication_date = models.DateField()
    conservation = models.IntegerField(choices=CONSERVATION_CHOICES)
    category = models.IntegerField(choices=CATEGORY_CHOICES)
    subject = models.ManyToManyField(Subject)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Modificado em', auto_now=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)

    # image = models.ImageField('Imagem', upload_to='materials', blank=True, null=True)

    def __str__(self):
        return self.title

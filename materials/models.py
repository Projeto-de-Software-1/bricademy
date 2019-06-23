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
        (1, 'POUCO USADO'),
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
    publication_date = models.DateField(blank=True, null=True)
    conservation = models.IntegerField(choices=CONSERVATION_CHOICES)
    category = models.IntegerField(choices=CATEGORY_CHOICES)
    subject = models.ManyToManyField(Subject)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Modificado em', auto_now=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(
        'Image', upload_to='materials/')
    deleted = models.IntegerField(default=0)
    deleted_at = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title


class Ad(models.Model):
    TYPE_CHOICES = [
        (0, 'VENDA'),
        (1, 'DOAÇÃO'),
        (2, 'EMPRÉSTIMO')
    ]

    duration = models.IntegerField(null=True, blank=True)
    address = models.CharField('Endereço', max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    loan_start = models.DateField(null=True, blank=True)
    material = models.OneToOneField(Material, on_delete=models.CASCADE)
    ad_type = models.IntegerField(choices=TYPE_CHOICES)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Modificado em', auto_now=True)
    request_accepted = models.ForeignKey(
        'Request', related_name='request_accepted', on_delete=models.CASCADE, blank=True, null=True)

    deleted = models.IntegerField(default=0)
    deleted_at = models.IntegerField(blank=True, null=True)

    class Meta:
        def __str__(self):
            return self.material


class Request(models.Model):
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Modificado em', auto_now=True)


class Complaint(models.Model):
    COMPLAINT_CHOICES = [
        (0, 'Conteúdo impróprio'),
        (1, 'Conteúdo não educacional'),
        (2, 'Outro')
    ]
    message = models.TextField(null=True, blank=True)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    complaint_type = models.IntegerField(choices=COMPLAINT_CHOICES)

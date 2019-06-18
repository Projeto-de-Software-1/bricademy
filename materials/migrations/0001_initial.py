# Generated by Django 2.2.1 on 2019-06-01 00:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.IntegerField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('loan_start', models.DateField(blank=True, null=True)),
                ('ad_type', models.IntegerField(choices=[(0, 'VENDA'), (1, 'DOAÇÃO'), (2, 'EMPRÉSTIMO')])),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100, verbose_name='Assunto')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materials.Ad')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Título')),
                ('author', models.CharField(max_length=50, verbose_name='Autor')),
                ('ISBN', models.CharField(blank=True, max_length=13, null=True, verbose_name='ISBN')),
                ('publishing_company', models.CharField(blank=True, max_length=50, null=True, verbose_name='Editora')),
                ('publication_date', models.DateField(blank=True, null=True)),
                ('conservation', models.IntegerField(choices=[(0, 'NOVO'), (1, 'SEMINOVO'), (2, 'USADO'), (3, 'MUITO USADO')])),
                ('category', models.IntegerField(choices=[(0, 'LIVRO'), (1, 'TESE'), (2, 'REVISTA'), (3, 'ARTIGO'), (4, 'RESUMO'), (5, 'OUTRO')])),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('subject', models.ManyToManyField(to='materials.Subject')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(blank=True, null=True)),
                ('complaint_type', models.IntegerField(choices=[(0, 'Conteúdo impróprio'), (1, 'Conteúdo não educacional'), (2, 'Outro')])),
                ('ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materials.Ad')),
            ],
        ),
        migrations.AddField(
            model_name='ad',
            name='material',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='materials.Material'),
        ),
        migrations.AddField(
            model_name='ad',
            name='request_accepted',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='request_accepted', to='materials.Request'),
        ),
    ]
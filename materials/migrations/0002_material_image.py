# Generated by Django 2.2.1 on 2019-06-01 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='materials', verbose_name='Image'),
        ),
    ]
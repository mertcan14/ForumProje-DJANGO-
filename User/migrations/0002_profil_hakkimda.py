# Generated by Django 3.1 on 2021-01-12 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profil',
            name='hakkimda',
            field=models.TextField(blank=True, max_length=400, null=True, verbose_name='Hakkınızda'),
        ),
    ]

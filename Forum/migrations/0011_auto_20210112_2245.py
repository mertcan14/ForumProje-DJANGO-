# Generated by Django 3.1 on 2021-01-12 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Forum', '0010_auto_20210112_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soru',
            name='catego',
            field=models.CharField(choices=[('education', 'Eğitim'), ('health', 'Sağlık'), ('economy', 'Ekonomi'), ('sport', 'Spor'), ('other', 'Diğer')], max_length=15),
        ),
    ]

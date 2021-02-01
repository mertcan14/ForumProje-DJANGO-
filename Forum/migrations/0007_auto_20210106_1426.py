# Generated by Django 3.1 on 2021-01-06 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Forum', '0006_auto_20210106_1423'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='begensoru',
            name='comment',
        ),
        migrations.AlterField(
            model_name='soru',
            name='catego',
            field=models.CharField(choices=[('education', 'Eğitim'), ('economy', 'Ekonomi'), ('other', 'Diğer'), ('sport', 'Spor'), ('health', 'Sağlık')], max_length=15),
        ),
    ]
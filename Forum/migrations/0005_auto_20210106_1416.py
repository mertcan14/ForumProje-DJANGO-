# Generated by Django 3.1 on 2021-01-06 11:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Forum', '0004_auto_20210106_0040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soru',
            name='catego',
            field=models.CharField(choices=[('health', 'Sağlık'), ('education', 'Eğitim'), ('other', 'Diğer'), ('sport', 'Spor'), ('economy', 'Ekonomi')], max_length=15),
        ),
        migrations.CreateModel(
            name='BegenSoru',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('repSor', models.CharField(max_length=200)),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('soru', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Forum.soru')),
            ],
        ),
    ]

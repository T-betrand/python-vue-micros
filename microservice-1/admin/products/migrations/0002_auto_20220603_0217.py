# Generated by Django 3.1.3 on 2022-06-03 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default='username', max_length=20),
        ),
    ]
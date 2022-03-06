# Generated by Django 3.2.4 on 2021-07-13 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(default=0, max_length=20),
        ),
    ]

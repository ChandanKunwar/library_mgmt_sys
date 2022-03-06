# Generated by Django 3.2.4 on 2021-07-15 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorPenName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='home.author')),
            ],
        ),
    ]
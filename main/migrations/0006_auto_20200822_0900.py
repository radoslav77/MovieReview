# Generated by Django 3.1 on 2020-08-22 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_movie_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='averidgerating',
            field=models.FloatField(default=0),
        ),
    ]

# Generated by Django 3.1 on 2020-08-22 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_movie_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.URLField(default=None, null=True),
        ),
    ]

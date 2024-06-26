# Generated by Django 5.0.3 on 2024-06-04 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_flixprimex', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='peliculas',
            name='url',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='series',
            name='url',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='peliculas',
            name='fecha_estreno',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='series',
            name='fecha_estreno',
            field=models.DateField(),
        ),
    ]

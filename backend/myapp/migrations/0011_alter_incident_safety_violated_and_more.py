# Generated by Django 4.2.5 on 2023-09-15 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_incident_situation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='Safety_violated',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='incident',
            name='Type_of_near_miss',
            field=models.CharField(max_length=20),
        ),
    ]
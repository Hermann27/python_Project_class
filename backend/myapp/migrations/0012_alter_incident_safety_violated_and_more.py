# Generated by Django 4.2.5 on 2023-09-15 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_alter_incident_safety_violated_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='Safety_violated',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='incident',
            name='Type_of_near_miss',
            field=models.CharField(max_length=30),
        ),
    ]

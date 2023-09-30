# Generated by Django 4.2.5 on 2023-09-14 17:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_alter_incident_incident_report_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='incident',
            name='Safety_violated',
            field=models.CharField(choices=[('No', 'No'), ('Yes', 'Yes'), ('N/A', 'N/A')], default=datetime.datetime(2023, 9, 14, 17, 43, 18, 114789, tzinfo=datetime.timezone.utc), max_length=20),
            preserve_default=False,
        ),
    ]

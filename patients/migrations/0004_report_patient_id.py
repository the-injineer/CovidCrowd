# Generated by Django 3.0.4 on 2020-03-21 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("patients", "0003_auto_20200321_0943"),
    ]

    operations = [
        migrations.AddField(
            model_name="report",
            name="patient_id",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]

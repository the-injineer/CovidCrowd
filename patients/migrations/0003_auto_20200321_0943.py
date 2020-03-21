# Generated by Django 3.0.4 on 2020-03-21 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("patients", "0002_auto_20200320_2043"),
    ]

    operations = [
        migrations.AddField(
            model_name="patient",
            name="government_id",
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name="patient",
            name="unique_id",
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name="patient",
            name="nationality",
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name="patient",
            name="status_change_date",
            field=models.DateField(null=True),
        ),
    ]

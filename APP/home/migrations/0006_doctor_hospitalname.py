# Generated by Django 4.0.4 on 2023-02-11 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_certificateissue'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='hospitalname',
            field=models.CharField(default='HospitalA', max_length=50),
        ),
    ]

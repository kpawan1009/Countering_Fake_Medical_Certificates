# Generated by Django 4.0.4 on 2023-02-11 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_certificate_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='username',
            field=models.CharField(default='vansh', max_length=50),
        ),
    ]

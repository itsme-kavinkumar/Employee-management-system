# Generated by Django 4.2.1 on 2023-06-11 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EMSAPI', '0014_alter_employeedata_role_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeedata',
            name='Netsalary',
            field=models.FloatField(default=0),
        ),
    ]

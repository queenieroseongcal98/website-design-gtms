# Generated by Django 3.1.5 on 2021-02-03 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20210202_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='address',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='method',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='receiver',
            field=models.CharField(max_length=255),
        ),
    ]

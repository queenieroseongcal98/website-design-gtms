# Generated by Django 3.1.5 on 2021-02-02 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20210202_1551'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='raddress',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='tdate',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='saddress',
            new_name='destination',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='sfee',
            new_name='fee',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='gname',
            new_name='goods',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='pmethod',
            new_name='method',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='rname',
            new_name='receiver',
        ),
    ]
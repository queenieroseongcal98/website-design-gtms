# Generated by Django 3.1.5 on 2021-02-02 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20210202_1531'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='sname',
            new_name='sender',
        ),
    ]

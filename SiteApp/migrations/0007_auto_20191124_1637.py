# Generated by Django 2.2.3 on 2019-11-24 21:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SiteApp', '0006_auto_20191120_1808'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quoterequest',
            name='destination',
        ),
        migrations.RemoveField(
            model_name='quoterequest',
            name='origin',
        ),
    ]

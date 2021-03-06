# Generated by Django 2.2.3 on 2019-09-25 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SiteApp', '0002_delete_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.IntegerField()),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('cell_number', models.BigIntegerField()),
                ('address', models.TextField()),
                ('designation', models.CharField(max_length=50)),
                ('salary', models.IntegerField()),
                ('date_of_join', models.DateField()),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='SiteApp.Department')),
            ],
        ),
    ]

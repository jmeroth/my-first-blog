# Generated by Django 2.0.3 on 2019-01-25 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_watersystem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watersystem',
            name='cities_served',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='watersystem',
            name='city_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='watersystem',
            name='counties_served',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='watersystem',
            name='gw_sw_code',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='watersystem',
            name='pws_activity_code',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='watersystem',
            name='pws_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='watersystem',
            name='pwsid',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='watersystem',
            name='state_code',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='watersystem',
            name='zip_code',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
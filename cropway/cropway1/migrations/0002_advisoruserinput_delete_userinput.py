# Generated by Django 5.1.7 on 2025-04-11 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cropway1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvisorUserInput',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('soil_type', models.CharField(max_length=100)),
                ('land_size', models.FloatField()),
                ('water_availability', models.CharField(max_length=100)),
                ('season', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='UserInput',
        ),
    ]

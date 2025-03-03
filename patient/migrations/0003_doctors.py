# Generated by Django 5.1.6 on 2025-02-24 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_diagnosis'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=20)),
            ],
        ),
    ]

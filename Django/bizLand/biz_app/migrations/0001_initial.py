# Generated by Django 5.1.3 on 2024-11-16 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clients', models.IntegerField()),
                ('project', models.IntegerField()),
                ('hoursOfSupport', models.IntegerField()),
                ('workers', models.IntegerField()),
            ],
        ),
    ]
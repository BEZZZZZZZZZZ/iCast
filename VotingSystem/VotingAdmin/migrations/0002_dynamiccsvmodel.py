# Generated by Django 4.2.6 on 2023-11-10 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VotingAdmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DynamicCSVModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field1', models.CharField(max_length=255)),
                ('field2', models.CharField(max_length=255)),
                ('field3', models.CharField(max_length=255)),
                ('field4', models.CharField(max_length=255)),
                ('field5', models.CharField(max_length=255)),
                ('field6', models.CharField(max_length=255)),
            ],
        ),
    ]

# Generated by Django 4.2.6 on 2023-10-24 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votingsystembase', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestform',
            name='organization',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='requestform',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default=None, max_length=100),
            preserve_default=False,
        ),
    ]

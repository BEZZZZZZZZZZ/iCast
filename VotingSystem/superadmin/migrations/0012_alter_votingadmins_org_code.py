# Generated by Django 4.2.6 on 2023-10-27 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superadmin', '0011_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='votingadmins',
            name='org_code',
            field=models.CharField(blank=True, default='JKlmnOaT', max_length=8),
        ),
    ]

# Generated by Django 4.2.7 on 2023-11-25 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('VotingAdmin', '0004_positions_election'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidateapplication',
            name='election',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='VotingAdmin.election'),
            preserve_default=False,
        ),
    ]

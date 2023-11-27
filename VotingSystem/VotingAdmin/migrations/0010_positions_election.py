# Generated by Django 4.2.7 on 2023-11-27 05:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('VotingAdmin', '0009_alter_candidateapplication_election'),
    ]

    operations = [
        migrations.AddField(
            model_name='positions',
            name='election',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='election', to='VotingAdmin.election'),
        ),
    ]

# Generated by Django 4.2.7 on 2023-11-16 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CSVUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('data', models.JSONField()),
                ('header_order', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Positions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pos_name', models.CharField(max_length=100)),
                ('Num_Candidates', models.IntegerField(default=0)),
                ('Total_votes', models.IntegerField(default=0)),
            ],
        ),
    ]

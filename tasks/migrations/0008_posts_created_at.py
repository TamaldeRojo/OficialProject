# Generated by Django 4.1.5 on 2023-02-10 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_carausel'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='created_at',
            field=models.DateField(auto_now=True),
        ),
    ]

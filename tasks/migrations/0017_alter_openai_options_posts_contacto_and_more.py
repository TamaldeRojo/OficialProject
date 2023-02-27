# Generated by Django 4.1.5 on 2023-02-27 07:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0016_openai_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='openai',
            options={'ordering': ('-created_at',)},
        ),
        migrations.AddField(
            model_name='posts',
            name='contacto',
            field=models.CharField(default='Sin contacto', max_length=250),
        ),
        migrations.AddField(
            model_name='posts',
            name='email_field',
            field=models.EmailField(default='SOME STRING', max_length=254),
        ),
        migrations.AddField(
            model_name='posts',
            name='fecha_prom',
            field=models.DateField(default=datetime.datetime(2023, 2, 27, 7, 19, 48, 472379, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='posts',
            name='presupuesto_prom',
            field=models.IntegerField(default=0),
        ),
    ]

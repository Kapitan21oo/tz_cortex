# Generated by Django 4.2.4 on 2023-08-29 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='album',
        ),
        migrations.AddField(
            model_name='song',
            name='albums',
            field=models.ManyToManyField(related_name='songs', to='catalog.album'),
        ),
    ]

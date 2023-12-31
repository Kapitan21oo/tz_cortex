# Generated by Django 4.2.4 on 2023-08-29 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_remove_song_album_song_albums'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='albums',
        ),
        migrations.RemoveField(
            model_name='song',
            name='track_number',
        ),
        migrations.CreateModel(
            name='AlbumSong',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('track_number', models.PositiveIntegerField()),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.album')),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.song')),
            ],
            options={
                'unique_together': {('album', 'song')},
            },
        ),
    ]

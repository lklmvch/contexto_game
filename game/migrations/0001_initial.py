# Generated by Django 5.1.4 on 2025-01-05 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('guessed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player', models.CharField(max_length=100)),
                ('score', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('started', 'Started'), ('finished', 'Finished')], default='started', max_length=20)),
                ('words', models.ManyToManyField(to='game.word')),
            ],
        ),
    ]

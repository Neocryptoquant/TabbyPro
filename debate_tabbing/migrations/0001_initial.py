# Generated by Django 5.1.4 on 2024-12-30 00:49

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adjudicator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('experience_level', models.CharField(choices=[('Novice', 'Novice'), ('Intermediate', 'Intermediate'), ('Expert', 'Expert')], max_length=50)),
                ('availability', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('wins', models.IntegerField(default=0)),
                ('speaker_points', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('format', models.CharField(choices=[('BP', 'British Parliamentary'), ('AP', 'Asian Parliamentary')], max_length=50)),
                ('pairing_method', models.CharField(choices=[('Random', 'Random'), ('Power', 'Power'), ('RoundRobin', 'Round Robin')], max_length=50)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', models.IntegerField()),
                ('result', models.JSONField(blank=True, null=True)),
                ('adjudicator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='debate_tabbing.adjudicator')),
                ('teams', models.ManyToManyField(related_name='matches', to='debate_tabbing.team')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches', to='debate_tabbing.tournament')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField()),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', to='debate_tabbing.match')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', to='debate_tabbing.team')),
            ],
        ),
        migrations.AddField(
            model_name='team',
            name='tournament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teams', to='debate_tabbing.tournament'),
        ),
        migrations.AddField(
            model_name='adjudicator',
            name='tournament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adjudicators', to='debate_tabbing.tournament'),
        ),
    ]

# Generated by Django 2.1.4 on 2019-06-03 20:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wlct', '0021_tournamentgamestatuslog'),
    ]

    operations = [
        migrations.CreateModel(
            name='MonthlyTemplateRotation',
            fields=[
                ('tournament_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wlct.Tournament')),
                ('current_template', models.IntegerField(default=0)),
            ],
            bases=('wlct.tournament',),
        ),
        migrations.CreateModel(
            name='MonthlyTemplateRotationMonth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('template', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='PromotionalRelegationLeague',
            fields=[
                ('tournament_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wlct.Tournament')),
                ('seasons', models.IntegerField(default=0)),
            ],
            bases=('wlct.tournament',),
        ),
        migrations.CreateModel(
            name='PromotionalRelegationLeagueSeason',
            fields=[
                ('tournament_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wlct.Tournament')),
                ('season_number', models.IntegerField(default=0)),
                ('groups', models.IntegerField(default=0)),
            ],
            bases=('wlct.tournament',),
        ),
        migrations.AddField(
            model_name='tournament',
            name='is_league',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='tournamentteam',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='promotionalrelegationleagueseason',
            name='parent_tournament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pr_parent_tournament', to='wlct.Tournament'),
        ),
    ]
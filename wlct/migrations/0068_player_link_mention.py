# Generated by Django 2.1.4 on 2020-02-08 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wlct', '0067_auto_20200207_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='link_mention',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
# Generated by Django 2.2.13 on 2020-07-04 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awc', '0003_challenge_extra'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requirement',
            name='extra',
            field=models.TextField(blank=True, default=''),
        ),
    ]

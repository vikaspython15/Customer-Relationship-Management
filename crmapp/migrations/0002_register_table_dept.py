# Generated by Django 3.2.5 on 2022-02-26 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='register_table',
            name='dept',
            field=models.CharField(default=' ', max_length=100),
            preserve_default=False,
        ),
    ]

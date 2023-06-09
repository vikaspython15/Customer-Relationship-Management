# Generated by Django 3.2.5 on 2022-03-06 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmapp', '0003_remove_register_table_dept'),
    ]

    operations = [
        migrations.AddField(
            model_name='register_table',
            name='about',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='register_table',
            name='added_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='register_table',
            name='age',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='register_table',
            name='city',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='register_table',
            name='gender',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='register_table',
            name='occupation',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='register_table',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profiles/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='register_table',
            name='update_on',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]

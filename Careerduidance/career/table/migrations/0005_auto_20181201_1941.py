# Generated by Django 2.1.3 on 2018-12-02 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0004_auto_20181201_1938'),
    ]

    operations = [
        migrations.RenameField(
            model_name='table',
            old_name='Title',
            new_name='School',
        ),
        migrations.RemoveField(
            model_name='table',
            name='body',
        ),
        migrations.AddField(
            model_name='table',
            name='Location',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='table',
            name='SchoolFee',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='table',
            name='StartYear',
            field=models.DateField(blank=True, null=True),
        ),
    ]

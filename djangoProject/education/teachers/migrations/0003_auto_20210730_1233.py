# Generated by Django 3.2.5 on 2021-07-30 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0002_rename_group_teachers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teachers',
            name='subject',
        ),
        migrations.AddField(
            model_name='teachers',
            name='age',
            field=models.IntegerField(default=25),
        ),
    ]

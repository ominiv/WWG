# Generated by Django 3.2.5 on 2021-11-22 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardApp', '0005_alter_board_mainphoto'),
    ]

    operations = [
        migrations.AddField(
            model_name='board2',
            name='mainphoto',
            field=models.ImageField(blank=True, null=True, upload_to='mainphoto'),
        ),
    ]
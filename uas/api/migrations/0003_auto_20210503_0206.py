# Generated by Django 3.1 on 2021-05-02 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210503_0206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='score1',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='game',
            name='score2',
            field=models.IntegerField(default=0),
        ),
    ]

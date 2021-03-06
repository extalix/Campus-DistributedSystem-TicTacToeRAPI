# Generated by Django 3.1 on 2021-05-02 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210503_0206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='player_one',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player1', to='api.player'),
        ),
        migrations.AlterField(
            model_name='game',
            name='player_two',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player2', to='api.player'),
        ),
    ]

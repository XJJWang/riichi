# Generated by Django 3.2.8 on 2022-01-17 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_auto_20220117_1551'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='ranking1',
        ),
        migrations.RemoveField(
            model_name='game',
            name='ranking2',
        ),
        migrations.RemoveField(
            model_name='game',
            name='ranking3',
        ),
        migrations.RemoveField(
            model_name='game',
            name='ranking4',
        ),
        migrations.AlterField(
            model_name='game',
            name='player1',
            field=models.ForeignKey(default='Unknown Player', on_delete=django.db.models.deletion.CASCADE, related_name='first_player', to='games.player', verbose_name='一位'),
        ),
        migrations.AlterField(
            model_name='game',
            name='player2',
            field=models.ForeignKey(default='Unknown Player', on_delete=django.db.models.deletion.CASCADE, related_name='second_player', to='games.player', verbose_name='二位'),
        ),
        migrations.AlterField(
            model_name='game',
            name='player3',
            field=models.ForeignKey(default='Unknown Player', on_delete=django.db.models.deletion.CASCADE, related_name='third_player', to='games.player', verbose_name='三位'),
        ),
        migrations.AlterField(
            model_name='game',
            name='player4',
            field=models.ForeignKey(default='Unknown Player', on_delete=django.db.models.deletion.CASCADE, related_name='fourth_player', to='games.player', verbose_name='四位'),
        ),
    ]
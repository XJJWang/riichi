# Generated by Django 3.2.8 on 2022-01-17 15:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_auto_20211103_1541'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='player',
            options={'ordering': ['-create_time'], 'verbose_name': '玩家', 'verbose_name_plural': '玩家'},
        ),
        migrations.AddField(
            model_name='player',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 1, 17, 15, 50, 35, 76878)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='is_actived',
            field=models.CharField(choices=[('True', '已激活'), ('False', '未激活')], default='未激活', max_length=24),
        ),
        migrations.AddField(
            model_name='player',
            name='password',
            field=models.CharField(default=1, max_length=256),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='game',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='name',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]

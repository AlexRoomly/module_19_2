# Generated by Django 5.1.1 on 2024-09-22 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0002_alter_game_buyer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='buyer',
            field=models.ManyToManyField(related_name='username', to='task1.buyer'),
        ),
    ]

# Generated by Django 4.0.4 on 2022-06-01 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_habit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='statistics',
            name='profile',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main_habit.profile'),
        ),
    ]

# Generated by Django 3.0.5 on 2020-04-28 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stackAPI', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='answer_count',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='question',
            name='view_count',
            field=models.CharField(default='', max_length=50),
        ),
    ]

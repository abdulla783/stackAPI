# Generated by Django 3.0.5 on 2020-04-28 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_title', models.CharField(max_length=300)),
                ('question_tag', models.CharField(max_length=250)),
                ('question_url', models.URLField(max_length=300)),
                ('question_view_count', models.IntegerField()),
                ('question_answer_count', models.IntegerField()),
            ],
        ),
    ]
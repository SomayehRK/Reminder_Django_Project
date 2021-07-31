# Generated by Django 3.2.5 on 2021-07-31 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0011_auto_20210731_1057'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='_status',
            field=models.CharField(choices=[('E', 'Expired'), ('C', 'Continuous')], db_column='status', default='C', max_length=1, verbose_name='status'),
        ),
    ]

# Generated by Django 3.2.5 on 2021-07-29 21:46

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_alter_task_managers'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='category',
            managers=[
                ('category_no_task', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='task',
            managers=[
                ('is_expired', django.db.models.manager.Manager()),
            ],
        ),
    ]
# Generated by Django 3.2.5 on 2021-07-28 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('priority', models.IntegerField(choices=[(0, 'بی اهمیت'), (1, 'کم اهمیت'), (2, 'توجه'), (3, 'قابل توجه'), (4, 'مهم'), (5, 'ضروری')], default=4)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deadline', models.DateTimeField()),
                ('category', models.ManyToManyField(related_name='category', to='todo.Category')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]

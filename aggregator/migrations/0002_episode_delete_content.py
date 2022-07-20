# Generated by Django 4.0.6 on 2022-07-20 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aggregator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('podcast_name', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('pub_date', models.DateTimeField()),
                ('link', models.URLField()),
                ('image', models.URLField()),
                ('guid', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Content',
        ),
    ]

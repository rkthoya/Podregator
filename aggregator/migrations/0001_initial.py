# Generated by Django 4.0.6 on 2022-07-19 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feed_name', models.CharField(max_length=200)),
                ('item_title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('pub_date', models.DateTimeField()),
                ('link', models.URLField()),
                ('image', models.URLField()),
                ('guid', models.CharField(max_length=200)),
            ],
        ),
    ]

# Generated by Django 2.2.5 on 2022-06-06 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('review', models.TextField()),
                ('accuracy', models.IntegerField()),
                ('cleanliness', models.IntegerField()),
                ('check_in', models.IntegerField()),
                ('communication', models.IntegerField()),
                ('location', models.IntegerField()),
                ('value', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

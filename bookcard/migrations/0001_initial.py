# Generated by Django 5.1.2 on 2024-10-30 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('about', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='')),
            ],
            options={
                'db_table': 'fairy_cards',
            },
        ),
    ]

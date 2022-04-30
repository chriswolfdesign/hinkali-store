# Generated by Django 4.0.3 on 2022-04-28 00:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False,
                                           verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('image',
                 models.ImageField(default='default/not-found.png', upload_to='photos/%Y/%m/%d/',
                                   verbose_name='Image')),
                ('added_date',
                 models.DateTimeField(default=datetime.datetime(2022, 4, 28, 0, 53, 43, 349000),
                                      verbose_name='Added')),
                ('price',
                 models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Price')),
                ('is_active', models.BooleanField(default=True, verbose_name='Showed to user')),
            ],
            options={
                'verbose_name': 'Dish',
                'verbose_name_plural': 'Dishes',
            },
        ),
    ]
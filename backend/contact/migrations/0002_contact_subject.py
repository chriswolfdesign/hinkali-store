# Generated by Django 4.0.3 on 2022-03-09 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='subject',
            field=models.CharField(default='str', max_length=255, verbose_name='Subject'),
            preserve_default=False,
        ),
    ]
# Generated by Django 4.1.7 on 2023-03-04 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='druh',
            name='jmeno',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='druh',
            name='text',
            field=models.CharField(max_length=500),
        ),
    ]

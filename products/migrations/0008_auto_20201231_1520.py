# Generated by Django 3.1.4 on 2020-12-31 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20201231_1511'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mtg_cards',
            name='color_identity',
        ),
        migrations.RemoveField(
            model_name='mtg_cards',
            name='colors',
        ),
    ]

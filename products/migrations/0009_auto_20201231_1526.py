# Generated by Django 3.1.4 on 2020-12-31 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20201231_1520'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mtg_cards',
            name='power',
        ),
        migrations.RemoveField(
            model_name='mtg_cards',
            name='toughness',
        ),
        migrations.AlterField(
            model_name='mtg_cards',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='mtg_cards',
            name='sku',
            field=models.CharField(max_length=254),
        ),
    ]

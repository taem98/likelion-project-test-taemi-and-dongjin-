# Generated by Django 2.1.7 on 2019-04-07 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_hit',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
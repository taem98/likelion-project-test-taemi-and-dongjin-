# Generated by Django 2.1.7 on 2019-04-11 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0004_auto_20190412_0031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='base',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
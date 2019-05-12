# Generated by Django 2.1.7 on 2019-05-12 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_product_product_hit'),
    ]

    operations = [
        migrations.RenameField(
            model_name='images',
            old_name='image',
            new_name='images',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_hit',
        ),
        migrations.AddField(
            model_name='base',
            name='hit',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='base',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]

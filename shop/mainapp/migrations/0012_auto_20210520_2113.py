# Generated by Django 3.1.7 on 2021-05-20 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0011_auto_20210520_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Curvature',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Загиб клюшки'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Flex',
            field=models.IntegerField(blank=True, null=True, verbose_name='Жесткость клюшки'),
        ),
    ]

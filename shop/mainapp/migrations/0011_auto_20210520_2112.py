# Generated by Django 3.1.7 on 2021-05-20 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_auto_20210520_2041'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Age',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Возраст'),
        ),
        migrations.AddField(
            model_name='product',
            name='Curvature',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Загиб'),
        ),
        migrations.AddField(
            model_name='product',
            name='Flex',
            field=models.IntegerField(blank=True, null=True, verbose_name='Жесткость'),
        ),
        migrations.AddField(
            model_name='product',
            name='Fullness',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Полнота коньков'),
        ),
        migrations.AddField(
            model_name='product',
            name='Material',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Материал'),
        ),
        migrations.AddField(
            model_name='product',
            name='Weight',
            field=models.FloatField(blank=True, null=True, verbose_name='Масса'),
        ),
    ]

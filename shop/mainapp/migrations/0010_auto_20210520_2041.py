# Generated by Django 3.1.7 on 2021-05-20 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_categoryfeature_featurevalidator_productfeatures'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='featurevalidator',
            name='category',
        ),
        migrations.RemoveField(
            model_name='featurevalidator',
            name='feature_key',
        ),
        migrations.RemoveField(
            model_name='productfeatures',
            name='feature',
        ),
        migrations.RemoveField(
            model_name='productfeatures',
            name='product',
        ),
        migrations.DeleteModel(
            name='CategoryFeature',
        ),
        migrations.DeleteModel(
            name='FeatureValidator',
        ),
        migrations.DeleteModel(
            name='ProductFeatures',
        ),
    ]

# Generated by Django 2.0.2 on 2018-08-29 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_newsprojectrelatedpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='newspage',
            name='drupal_id',
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
    ]

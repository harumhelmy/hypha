# Generated by Django 2.0.13 on 2019-07-09 11:14

from django.db import migrations, models
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_metacategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='metacategory',
            name='available_to_applications',
            field=models.BooleanField(default=True, help_text='Make available for applications'),
        ),
        migrations.AddField(
            model_name='metacategory',
            name='filter_on_dashboard',
            field=models.BooleanField(default=True, help_text='Make available to filter on dashboard'),
        ),
        migrations.AddField(
            model_name='metacategory',
            name='help_text',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='metacategory',
            name='is_archived',
            field=models.BooleanField(default=False, verbose_name='Archived'),
        ),
    ]

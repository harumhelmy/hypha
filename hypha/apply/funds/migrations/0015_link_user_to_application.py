# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-01 16:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import hypha.apply.categories.blocks
import wagtail.core.blocks
import wagtail.core.blocks.static_block
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('funds', '0014_add_meta_names'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationsubmission',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='fundtype',
            name='confirmation_text_extra',
            field=models.TextField(blank=True, help_text='Additional text for the application confirmation message.'),
        ),
        migrations.AddField(
            model_name='fundtype',
            name='from_address',
            field=models.CharField(blank=True, max_length=255, verbose_name='from address'),
        ),
        migrations.AddField(
            model_name='fundtype',
            name='subject',
            field=models.CharField(blank=True, max_length=255, verbose_name='subject'),
        ),
        migrations.AddField(
            model_name='fundtype',
            name='to_address',
            field=models.CharField(blank=True, help_text='Optional - form submissions will be emailed to these addresses. Separate multiple addresses by comma.', max_length=255, verbose_name='to address'),
        ),
        migrations.AddField(
            model_name='labtype',
            name='confirmation_text_extra',
            field=models.TextField(blank=True, help_text='Additional text for the application confirmation message.'),
        ),
        migrations.AddField(
            model_name='labtype',
            name='from_address',
            field=models.CharField(blank=True, max_length=255, verbose_name='from address'),
        ),
        migrations.AddField(
            model_name='labtype',
            name='subject',
            field=models.CharField(blank=True, max_length=255, verbose_name='subject'),
        ),
        migrations.AddField(
            model_name='labtype',
            name='to_address',
            field=models.CharField(blank=True, help_text='Optional - form submissions will be emailed to these addresses. Separate multiple addresses by comma.', max_length=255, verbose_name='to address'),
        ),
        migrations.AlterField(
            model_name='applicationform',
            name='form_fields',
            field=wagtail.core.fields.StreamField((('text_markup', wagtail.core.blocks.RichTextBlock(group='Other', label='Paragraph')), ('char', wagtail.core.blocks.StructBlock((('field_label', wagtail.core.blocks.CharBlock(label='Label')), ('help_text', wagtail.core.blocks.TextBlock(label='Help text', required=False)), ('required', wagtail.core.blocks.BooleanBlock(label='Required', required=False)), ('format', wagtail.core.blocks.ChoiceBlock(choices=[('email', 'Email'), ('url', 'URL')], label='Format', required=False)), ('default_value', wagtail.core.blocks.CharBlock(label='Default value', required=False))), group='Fields')), ('text', wagtail.core.blocks.StructBlock((('field_label', wagtail.core.blocks.CharBlock(label='Label')), ('help_text', wagtail.core.blocks.TextBlock(label='Help text', required=False)), ('required', wagtail.core.blocks.BooleanBlock(label='Required', required=False)), ('default_value', wagtail.core.blocks.TextBlock(label='Default value', required=False))), group='Fields')), ('number', wagtail.core.blocks.StructBlock((('field_label', wagtail.core.blocks.CharBlock(label='Label')), ('help_text', wagtail.core.blocks.TextBlock(label='Help text', required=False)), ('required', wagtail.core.blocks.BooleanBlock(label='Required', required=False)), ('default_value', wagtail.core.blocks.CharBlock(label='Default value', required=False))), group='Fields')), ('checkbox', wagtail.core.blocks.StructBlock((('field_label', wagtail.core.blocks.CharBlock(label='Label')), ('help_text', wagtail.core.blocks.TextBlock(label='Help text', required=False)), ('default_value', wagtail.core.blocks.BooleanBlock(required=False))), group='Fields')), ('radios', wagtail.core.blocks.StructBlock((('field_label', wagtail.core.blocks.CharBlock(label='Label')), ('help_text', wagtail.core.blocks.TextBlock(label='Help text', required=False)), ('required', wagtail.core.blocks.BooleanBlock(label='Required', required=False)), ('choices', wagtail.core.blocks.ListBlock(wagtail.core.blocks.CharBlock(label='Choice')))), group='Fields')), ('dropdown', wagtail.core.blocks.StructBlock((('field_label', wagtail.core.blocks.CharBlock(label='Label')), ('help_text', wagtail.core.blocks.TextBlock(label='Help text', required=False)), ('required', wagtail.core.blocks.BooleanBlock(label='Required', required=False)), ('choices', wagtail.core.blocks.ListBlock(wagtail.core.blocks.CharBlock(label='Choice')))), group='Fields')), ('checkboxes', wagtail.core.blocks.StructBlock((('field_label', wagtail.core.blocks.CharBlock(label='Label')), ('help_text', wagtail.core.blocks.TextBlock(label='Help text', required=False)), ('required', wagtail.core.blocks.BooleanBlock(label='Required', required=False)), ('checkboxes', wagtail.core.blocks.ListBlock(wagtail.core.blocks.CharBlock(label='Checkbox')))), group='Fields')), ('date', wagtail.core.blocks.StructBlock((('field_label', wagtail.core.blocks.CharBlock(label='Label')), ('help_text', wagtail.core.blocks.TextBlock(label='Help text', required=False)), ('required', wagtail.core.blocks.BooleanBlock(label='Required', required=False)), ('default_value', wagtail.core.blocks.DateBlock(required=False))), group='Fields')), ('time', wagtail.core.blocks.StructBlock((('field_label', wagtail.core.blocks.CharBlock(label='Label')), ('help_text', wagtail.core.blocks.TextBlock(label='Help text', required=False)), ('required', wagtail.core.blocks.BooleanBlock(label='Required', required=False)), ('default_value', wagtail.core.blocks.TimeBlock(required=False))), group='Fields')), ('datetime', wagtail.core.blocks.StructBlock((('field_label', wagtail.core.blocks.CharBlock(label='Label')), ('help_text', wagtail.core.blocks.TextBlock(label='Help text', required=False)), ('required', wagtail.core.blocks.BooleanBlock(label='Required', required=False)), ('default_value', wagtail.core.blocks.DateTimeBlock(required=False))), group='Fields')), ('image', wagtail.core.blocks.StructBlock((('field_label', wagtail.core.blocks.CharBlock(label='Label')), ('help_text', wagtail.core.blocks.TextBlock(label='Help text', required=False)), ('required', wagtail.core.blocks.BooleanBlock(label='Required', required=False))), group='Fields')), ('file', wagtail.core.blocks.StructBlock((('field_label', wagtail.core.blocks.CharBlock(label='Label')), ('help_text', wagtail.core.blocks.TextBlock(label='Help text', required=False)), ('required', wagtail.core.blocks.BooleanBlock(label='Required', required=False))), group='Fields')), ('rich_text', wagtail.core.blocks.StructBlock((('field_label', wagtail.core.blocks.CharBlock(label='Label')), ('help_text', wagtail.core.blocks.TextBlock(label='Help text', required=False)), ('required', wagtail.core.blocks.BooleanBlock(label='Required', required=False)), ('default_value', wagtail.core.blocks.TextBlock(label='Default value', required=False))), group='Fields')), ('category', wagtail.core.blocks.StructBlock((('field_label', wagtail.core.blocks.CharBlock(help_text='Leave blank to use the default Category label', label='Label', required=False)), ('help_text', wagtail.core.blocks.TextBlock(label='Leave blank to use the default Category help text', required=False)), ('required', wagtail.core.blocks.BooleanBlock(label='Required', required=False)), ('category', hypha.apply.categories.blocks.ModelChooserBlock('categories.Category')), ('multi', wagtail.core.blocks.BooleanBlock(label='Multi select', required=False))), group='Custom')), ('title', wagtail.core.blocks.StructBlock((('field_label', wagtail.core.blocks.CharBlock(label='Label')), ('help_text', wagtail.core.blocks.TextBlock(label='Help text', required=False)), ('info', wagtail.core.blocks.static_block.StaticBlock())), group='Required')), ('value', wagtail.core.blocks.StructBlock((('field_label', wagtail.core.blocks.CharBlock(label='Label')), ('help_text', wagtail.core.blocks.TextBlock(label='Help text', required=False)), ('info', wagtail.core.blocks.static_block.StaticBlock())), group='Required')), ('email', wagtail.core.blocks.StructBlock((('field_label', wagtail.core.blocks.CharBlock(label='Label')), ('help_text', wagtail.core.blocks.TextBlock(label='Help text', required=False)), ('info', wagtail.core.blocks.static_block.StaticBlock())), group='Required')), ('full_name', wagtail.core.blocks.StructBlock((('field_label', wagtail.core.blocks.CharBlock(label='Label')), ('help_text', wagtail.core.blocks.TextBlock(label='Help text', required=False)), ('info', wagtail.core.blocks.static_block.StaticBlock())), group='Required')))),
        ),
    ]

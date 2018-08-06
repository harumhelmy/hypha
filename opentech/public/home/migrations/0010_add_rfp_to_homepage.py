# Generated by Django 2.0.2 on 2018-08-03 10:44

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('home', '0009_django2_update'),
    ]

    operations = [
        migrations.CreateModel(
            name='PromotedRFPs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='homepage',
            name='rfps_intro',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='rfps_title',
            field=models.CharField(default='Requests For Partners', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='promotedrfps',
            name='source_page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='promoted_rfps', to='home.HomePage'),
        ),
        migrations.AlterUniqueTogether(
            name='promotedrfps',
            unique_together={('page',)},
        ),
    ]
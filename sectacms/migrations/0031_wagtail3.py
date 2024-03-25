# Generated by Django 4.0.6 on 2022-07-29 19:27

import sectacms.fields
import django.core.serializers.json
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sectacms', '0030_alter_sectatag_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carouselslide',
            name='content',
            field=sectacms.fields.sectaStreamField(blank=True, use_json_field=True),
        ),
        migrations.AlterField(
            model_name='sectapage',
            name='content_walls',
            field=sectacms.fields.sectaStreamField(blank=True, use_json_field=True, verbose_name='Content Walls'),
        ),
        migrations.AlterField(
            model_name='sectasessionformsubmission',
            name='form_data',
            field=models.JSONField(encoder=django.core.serializers.json.DjangoJSONEncoder),
        ),
        migrations.AlterField(
            model_name='contentwall',
            name='content',
            field=sectacms.fields.sectaStreamField(blank=True, use_json_field=True, verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='footer',
            name='content',
            field=sectacms.fields.sectaStreamField(blank=True, use_json_field=True, verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='navbar',
            name='menu_items',
            field=sectacms.fields.sectaStreamField(blank=True, use_json_field=True, verbose_name='Navigation links'),
        ),
        migrations.AlterField(
            model_name='reusablecontent',
            name='content',
            field=sectacms.fields.sectaStreamField(blank=True, use_json_field=True, verbose_name='content'),
        ),
    ]

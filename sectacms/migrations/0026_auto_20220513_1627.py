# Generated by Django 3.2.13 on 2022-05-13 20:27

import sectacms.blocks.base_blocks
import sectacms.blocks.html_blocks
import sectacms.fields
from django.db import migrations
import wagtail.contrib.table_block.blocks
import wagtail.blocks
import wagtail.fields
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.images.blocks
import wagtail.snippets.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('sectacms', '0025_delete_socialmediasettings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carouselslide',
            name='content',
            field=sectacms.fields.sectaStreamField([], blank=True),
        ),
        migrations.AlterField(
            model_name='contentwall',
            name='content',
            field=sectacms.fields.sectaStreamField([], blank=True, verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='footer',
            name='content',
            field=sectacms.fields.sectaStreamField([], blank=True, verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='reusablecontent',
            name='content',
            field=sectacms.fields.sectaStreamField([], blank=True, verbose_name='content'),
        ),
    ]
# Generated by Django 2.2.9 on 2019-12-27 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sectacms', '0016_auto_20191025_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='generalsettings',
            name='external_new_tab',
            field=models.BooleanField(default=False, verbose_name='Open all external links in new tab'),
        ),
    ]

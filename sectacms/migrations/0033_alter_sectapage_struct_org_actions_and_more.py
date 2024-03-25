# Generated by Django 4.0.7 on 2022-08-08 19:44

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sectacms', '0032_accordion_accordionpanel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sectapage',
            name='struct_org_actions',
            field=wagtail.fields.StreamField([('actions', wagtail.blocks.StructBlock([('action_type', wagtail.blocks.ChoiceBlock(choices=[('OrderAction', 'OrderAction'), ('ReserveAction', 'ReserveAction')], verbose_name='Action Type')), ('target', wagtail.blocks.URLBlock(verbose_name='Target URL')), ('language', wagtail.blocks.CharBlock(default='en-US', help_text='If the action is offered in multiple languages, create separate actions for each language.', verbose_name='Language')), ('result_type', wagtail.blocks.ChoiceBlock(choices=[('Reservation', 'Reservation'), ('BusReservation', 'BusReservation'), ('EventReservation', 'EventReservation'), ('FlightReservation', 'FlightReservation'), ('FoodEstablishmentReservation', 'FoodEstablishmentReservation'), ('LodgingReservation', 'LodgingReservation'), ('RentalCarReservation', 'RentalCarReservation'), ('ReservationPackage', 'ReservationPackage'), ('TaxiReservation', 'TaxiReservation'), ('TrainReservation', 'TrainReservation')], help_text='Leave blank for OrderAction', required=False, verbose_name='Result Type')), ('result_name', wagtail.blocks.CharBlock(help_text='Example: "Reserve a table", "Book an appointment", etc.', required=False, verbose_name='Result Name')), ('extra_json', wagtail.blocks.RawHTMLBlock(form_classname='monospace', help_text='Additional JSON-LD inserted into the Action dictionary. Must be properties of https://schema.org/Action.', required=False, verbose_name='Additional action markup'))]))], blank=True, use_json_field=True, verbose_name='Actions'),
        ),
        migrations.AlterField(
            model_name='sectapage',
            name='struct_org_hours',
            field=wagtail.fields.StreamField([('hours', wagtail.blocks.StructBlock([('days', wagtail.blocks.MultipleChoiceBlock(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], help_text='For late night hours past 23:59, define each day in a separate block.', verbose_name='Days')), ('start_time', wagtail.blocks.TimeBlock(verbose_name='Opening time')), ('end_time', wagtail.blocks.TimeBlock(verbose_name='Closing time'))]))], blank=True, use_json_field=True, verbose_name='Hours of operation'),
        ),
    ]
"""
Enhancements to wagtail.contrib.forms.
"""

import csv
import os
from django import forms
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ValidationError
from django.db import models
from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _
from wagtail.contrib.forms.views import (
    SubmissionsListView as WagtailSubmissionsListView,
)
from wagtail.contrib.forms.forms import FormBuilder
from wagtail.contrib.forms.models import AbstractFormField

from sectacms.settings import Secta_settings
from sectacms.utils import attempt_protected_media_value_conversion

FORM_FIELD_CHOICES = (
    (
        _("Text"),
        (
            ("singleline", _("Single line text")),
            ("multiline", _("Multi-line text")),
            ("email", _("Email")),
            ("number", _("Number - only allows integers")),
            ("url", _("URL")),
        ),
    ),
    (
        _("Choice"),
        (
            ("checkboxes", _("Checkboxes")),
            ("dropdown", _("Drop down")),
            ("radio", _("Radio buttons")),
            ("multiselect", _("Multiple select")),
            ("checkbox", _("Single checkbox")),
        ),
    ),
    (
        _("Date & Time"),
        (
            ("date", _("Date")),
            ("time", _("Time")),
            ("datetime", _("Date and time")),
        ),
    ),
    (
        _("File Upload"),
        (("file", _("Secure File - login required to access uploaded files")),),
    ),
    (
        _("Other"),
        (("hidden", _("Hidden field")),),
    ),
)


# Files


class SecureFileField(forms.FileField):
    custom_error_messages = {
        "blacklist_file": _("Submitted file is not allowed."),
        "whitelist_file": _("Submitted file is not allowed."),
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.error_messages.update(self.custom_error_messages)

    def validate(self, value):
        super(SecureFileField, self).validate(value)
        if value:
            self._check_whitelist(value)
            self._check_blacklist(value)

    def _check_whitelist(self, value):
        if Secta_settings.Secta_PROTECTED_MEDIA_UPLOAD_WHITELIST:
            if (
                os.path.splitext(value.name)[1].lower()
                not in Secta_settings.Secta_PROTECTED_MEDIA_UPLOAD_WHITELIST
            ):
                raise ValidationError(self.error_messages["whitelist_file"])

    def _check_blacklist(self, value):
        if Secta_settings.Secta_PROTECTED_MEDIA_UPLOAD_BLACKLIST:
            if (
                os.path.splitext(value.name)[1].lower()
                in Secta_settings.Secta_PROTECTED_MEDIA_UPLOAD_BLACKLIST
            ):
                raise ValidationError(self.error_messages["blacklist_file"])


# Date


class sectaDateInput(forms.DateInput):
    template_name = "sectacms/formfields/date.html"


class sectaDateField(forms.DateField):
    widget = sectaDateInput()


# Datetime


class sectaDateTimeInput(forms.DateTimeInput):
    template_name = "sectacms/formfields/datetime.html"


class sectaDateTimeField(forms.DateTimeField):
    widget = sectaDateTimeInput()
    input_formats = [
        "%Y-%m-%dT%H:%M",
        "%m/%d/%Y %I:%M %p",
        "%m/%d/%Y %I:%M%p",
        "%m/%d/%Y %H:%M",
    ]


# Time


class sectaTimeInput(forms.TimeInput):
    template_name = "sectacms/formfields/time.html"


class sectaTimeField(forms.TimeField):
    widget = sectaTimeInput()
    input_formats = ["%H:%M", "%I:%M %p", "%I:%M%p"]


class sectaFormBuilder(FormBuilder):
    """
    Enhance wagtail FormBuilder with additional custom fields.
    """

    def create_file_field(self, field, options):
        return SecureFileField(**options)

    def create_date_field(self, field, options):
        return sectaDateField(**options)

    def create_datetime_field(self, field, options):
        return sectaDateTimeField(**options)

    def create_time_field(self, field, options):
        return sectaTimeField(**options)


class sectaSubmissionsListView(WagtailSubmissionsListView):
    def get_csv_response(self, context):
        filename = self.get_csv_filename()
        response = HttpResponse(content_type="text/csv; charset=utf-8")
        response["Content-Disposition"] = "attachment;filename={}".format(
            filename
        )

        writer = csv.writer(response)
        writer.writerow(context["data_headings"])
        for data_row in context["data_rows"]:
            modified_data_row = []
            for cell in data_row:
                modified_cell = attempt_protected_media_value_conversion(
                    self.request, cell
                )
                modified_data_row.append(modified_cell)

            writer.writerow(modified_data_row)
        return response


class sectaFormField(AbstractFormField):
    class Meta:
        abstract = True

    field_type = models.CharField(
        verbose_name=_("field type"),
        max_length=16,
        choices=FORM_FIELD_CHOICES,
        blank=False,
        default="Single line text",
    )


class SearchForm(forms.Form):
    s = forms.CharField(
        max_length=255,
        required=False,
        label=_("Search"),
    )
    t = forms.CharField(
        widget=forms.HiddenInput,
        max_length=255,
        required=False,
        label=_("Page type"),
    )


def get_page_model_choices():
    """
    Returns a list of tuples of all creatable secta pages
    in the format of (app_label:model, "Verbose Name")
    """
    from sectacms.models import get_page_models

    rval = []
    for page in get_page_models():
        if page.is_creatable:
            ct = ContentType.objects.get_for_model(page)
            rval.append((f"{ct.app_label}:{ct.model}", ct.name))
    return rval

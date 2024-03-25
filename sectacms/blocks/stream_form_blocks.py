from django.utils.translation import gettext_lazy as _
from wagtail import blocks

from sectacms.wagtail_flexible_forms import blocks as form_blocks
from sectacms.blocks.base_blocks import BaseBlock, sectaAdvSettings
from sectacms.forms import (
    sectaDateField,
    sectaDateInput,
    sectaDateTimeField,
    sectaDateTimeInput,
    sectaTimeField,
    sectaTimeInput,
    SecureFileField,
)


class sectaFormAdvSettings(sectaAdvSettings):
    condition_trigger_id = blocks.CharBlock(
        required=False,
        max_length=255,
        label=_("Condition Trigger ID"),
        help_text=_(
            'The "Custom ID" of another field that that will trigger this '
            "field to be shown/hidden."
        ),
    )
    condition_trigger_value = blocks.CharBlock(
        required=False,
        max_length=255,
        label=_("Condition Trigger Value"),
        help_text=_(
            'The value of the field in "Condition Trigger ID" that will '
            "trigger this field to be shown."
        ),
    )


class FormBlockMixin(BaseBlock):
    class Meta:
        abstract = True

    advsettings_class = sectaFormAdvSettings


class sectaStreamFormFieldBlock(
    form_blocks.OptionalFormFieldBlock, FormBlockMixin
):
    pass


class sectaStreamFormCharFieldBlock(
    form_blocks.CharFieldBlock, FormBlockMixin
):
    class Meta:
        label = _("Text or Email input")
        icon = "cr-window-minimize"


class sectaStreamFormTextFieldBlock(
    form_blocks.TextFieldBlock, FormBlockMixin
):
    class Meta:
        label = _("Multi-line text")
        icon = "cr-align-left"


class sectaStreamFormNumberFieldBlock(
    form_blocks.NumberFieldBlock, FormBlockMixin
):
    class Meta:
        label = _("Numbers only")
        icon = "cr-hashtag"


class sectaStreamFormCheckboxFieldBlock(
    form_blocks.CheckboxFieldBlock, FormBlockMixin
):
    class Meta:
        label = _("Single Checkbox")
        icon = "cr-check-square-o"


class sectaStreamFormRadioButtonsFieldBlock(
    form_blocks.RadioButtonsFieldBlock, FormBlockMixin
):
    class Meta:
        label = _("Radios")
        icon = "list-ul"


class sectaStreamFormDropdownFieldBlock(
    form_blocks.DropdownFieldBlock, FormBlockMixin
):
    class Meta:
        label = _("Dropdown")
        icon = "cr-list-alt"


class sectaStreamFormCheckboxesFieldBlock(
    form_blocks.CheckboxesFieldBlock, FormBlockMixin
):
    class Meta:
        label = _("Checkboxes")
        icon = "list-ul"


class sectaStreamFormDateFieldBlock(
    form_blocks.DateFieldBlock, FormBlockMixin
):
    class Meta:
        label = _("Date")
        icon = "date"

    field_class = sectaDateField
    widget = sectaDateInput


class sectaStreamFormTimeFieldBlock(
    form_blocks.TimeFieldBlock, FormBlockMixin
):
    class Meta:
        label = _("Time")
        icon = "time"

    field_class = sectaTimeField
    widget = sectaTimeInput


class sectaStreamFormDateTimeFieldBlock(
    form_blocks.DateTimeFieldBlock, FormBlockMixin
):
    class Meta:
        label = _("Date and Time")
        icon = "date"

    field_class = sectaDateTimeField
    widget = sectaDateTimeInput


class sectaStreamFormImageFieldBlock(
    form_blocks.ImageFieldBlock, FormBlockMixin
):
    class Meta:
        label = _("Image Upload")
        icon = "image"


class sectaStreamFormFileFieldBlock(
    form_blocks.FileFieldBlock, FormBlockMixin
):
    class Meta:
        label = _("Secure File Upload")
        icon = "upload"

    field_class = SecureFileField


class sectaStreamFormStepBlock(form_blocks.FormStepBlock):
    form_fields = blocks.StreamBlock()

    def __init__(self, local_blocks=None, **kwargs):
        super().__init__(
            local_blocks=[("form_fields", blocks.StreamBlock(local_blocks))]
        )

"""
Blocks module entry point. Used to cleanly organize blocks into
individual files based on purpose, but provide them all as a
single `blocks` module.
"""

from django.utils.translation import gettext_lazy as _

from wagtail import blocks

from .stream_form_blocks import (
    sectaStreamFormCharFieldBlock,
    sectaStreamFormCheckboxesFieldBlock,
    sectaStreamFormCheckboxFieldBlock,
    sectaStreamFormDateFieldBlock,
    sectaStreamFormDateTimeFieldBlock,
    sectaStreamFormDropdownFieldBlock,
    sectaStreamFormFileFieldBlock,
    sectaStreamFormImageFieldBlock,
    sectaStreamFormNumberFieldBlock,
    sectaStreamFormRadioButtonsFieldBlock,
    sectaStreamFormStepBlock,
    sectaStreamFormTextFieldBlock,
    sectaStreamFormTimeFieldBlock,
)
from .html_blocks import (
    ButtonBlock,
    EmbedGoogleMapBlock,
    ImageBlock,
    ImageLinkBlock,
    DownloadBlock,
    EmbedVideoBlock,
    PageListBlock,
    PagePreviewBlock,
    QuoteBlock,
    RichTextBlock,
    TableBlock,
)
from .content_blocks import (  # noqa
    AccordionBlock,
    CardBlock,
    CarouselBlock,
    ContentWallBlock,
    FilmStripBlock,
    ImageGalleryBlock,
    ModalBlock,
    NavDocumentLinkWithSubLinkBlock,
    NavExternalLinkWithSubLinkBlock,
    NavPageLinkWithSubLinkBlock,
    PriceListBlock,
    ReusableContentBlock,
)
from .layout_blocks import CardGridBlock, GridBlock, HeroBlock
from .base_blocks import (  # noqa
    BaseBlock,
    BaseLayoutBlock,
    BaseLinkBlock,
    ClassifierTermChooserBlock,
    sectaAdvColumnSettings,
    sectaAdvSettings,
    sectaAdvTrackingSettings,
    CollectionChooserBlock,
)

# Collections of blocks commonly used together.

HTML_STREAMBLOCKS = [
    ("text", RichTextBlock(icon="cr-font")),
    ("button", ButtonBlock()),
    ("image", ImageBlock()),
    ("image_link", ImageLinkBlock()),
    (
        "html",
        blocks.RawHTMLBlock(
            icon="code",
            form_classname="monospace",
            label=_("HTML"),
        ),
    ),
    ("download", DownloadBlock()),
    ("embed_video", EmbedVideoBlock()),
    ("quote", QuoteBlock()),
    ("table", TableBlock()),
    ("google_map", EmbedGoogleMapBlock()),
    ("page_list", PageListBlock()),
    ("page_preview", PagePreviewBlock()),
]

CONTENT_STREAMBLOCKS = HTML_STREAMBLOCKS + [
    ("accordion", AccordionBlock()),
    ("card", CardBlock()),
    ("carousel", CarouselBlock()),
    ("film_strip", FilmStripBlock()),
    ("image_gallery", ImageGalleryBlock()),
    ("modal", ModalBlock(HTML_STREAMBLOCKS)),
    ("pricelist", PriceListBlock()),
    ("reusable_content", ReusableContentBlock()),
]

NAVIGATION_STREAMBLOCKS = [
    ("page_link", NavPageLinkWithSubLinkBlock()),
    ("external_link", NavExternalLinkWithSubLinkBlock()),
    ("document_link", NavDocumentLinkWithSubLinkBlock()),
]

BASIC_LAYOUT_STREAMBLOCKS = [
    ("row", GridBlock(HTML_STREAMBLOCKS)),
    (
        "html",
        blocks.RawHTMLBlock(
            icon="code", form_classname="monospace", label=_("HTML")
        ),
    ),
]

LAYOUT_STREAMBLOCKS = [
    (
        "hero",
        HeroBlock(
            [
                ("row", GridBlock(CONTENT_STREAMBLOCKS)),
                (
                    "cardgrid",
                    CardGridBlock(
                        [
                            ("card", CardBlock()),
                        ]
                    ),
                ),
                (
                    "html",
                    blocks.RawHTMLBlock(
                        icon="code", form_classname="monospace", label=_("HTML")
                    ),
                ),
            ]
        ),
    ),
    ("row", GridBlock(CONTENT_STREAMBLOCKS)),
    (
        "cardgrid",
        CardGridBlock(
            [
                ("card", CardBlock()),
            ]
        ),
    ),
    (
        "html",
        blocks.RawHTMLBlock(
            icon="code", form_classname="monospace", label=_("HTML")
        ),
    ),
]

STREAMFORM_FIELDBLOCKS = [
    ("sf_singleline", sectaStreamFormCharFieldBlock(group=_("Fields"))),
    ("sf_multiline", sectaStreamFormTextFieldBlock(group=_("Fields"))),
    ("sf_number", sectaStreamFormNumberFieldBlock(group=_("Fields"))),
    ("sf_checkboxes", sectaStreamFormCheckboxesFieldBlock(group=_("Fields"))),
    ("sf_radios", sectaStreamFormRadioButtonsFieldBlock(group=_("Fields"))),
    ("sf_dropdown", sectaStreamFormDropdownFieldBlock(group=_("Fields"))),
    ("sf_checkbox", sectaStreamFormCheckboxFieldBlock(group=_("Fields"))),
    ("sf_date", sectaStreamFormDateFieldBlock(group=_("Fields"))),
    ("sf_time", sectaStreamFormTimeFieldBlock(group=_("Fields"))),
    ("sf_datetime", sectaStreamFormDateTimeFieldBlock(group=_("Fields"))),
    ("sf_image", sectaStreamFormImageFieldBlock(group=_("Fields"))),
    ("sf_file", sectaStreamFormFileFieldBlock(group=_("Fields"))),
]

STREAMFORM_BLOCKS = [
    (
        "step",
        sectaStreamFormStepBlock(STREAMFORM_FIELDBLOCKS + HTML_STREAMBLOCKS),
    ),
]

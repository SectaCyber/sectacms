from sectacms.models.page_models import sectaPage
from modelcluster.fields import ParentalKey
from sectacms.forms import sectaFormField
from sectacms.models import (
    sectaArticlePage,
    sectaArticleIndexPage,
    sectaEventIndexPage,
    sectaEventPage,
    sectaEventOccurrence,
    sectaEmail,
    sectaFormPage,
    sectaLocationIndexPage,
    sectaLocationPage,
    sectaStreamFormPage,
    sectaWebPage,
)


class ArticlePage(sectaArticlePage):
    class Meta:
        verbose_name = "Article"
        ordering = [
            "-first_published_at",
        ]

    # Only allow this page to be created beneath an ArticleIndexPage.
    parent_page_types = ["testapp.ArticleIndexPage"]

    template = "sectacms/pages/article_page.html"
    search_template = "sectacms/pages/article_page.search.html"


class ArticleIndexPage(sectaArticleIndexPage):
    class Meta:
        verbose_name = "Article Landing Page"

    index_order_by_default = ""

    # Override to specify custom index ordering choice/default.
    index_query_pagemodel = "testapp.ArticlePage"

    # Only allow ArticlePages beneath this page.
    subpage_types = ["testapp.ArticlePage"]

    template = "sectacms/pages/article_index_page.html"


class FormPage(sectaFormPage):
    class Meta:
        verbose_name = "Form"

    template = "sectacms/pages/form_page.html"


class FormPageField(sectaFormField):
    class Meta:
        ordering = ["sort_order"]

    page = ParentalKey("FormPage", related_name="form_fields")


class FormConfirmEmail(sectaEmail):
    page = ParentalKey("FormPage", related_name="confirmation_emails")


class WebPage(sectaWebPage):
    class Meta:
        verbose_name = "Web Page"

    template = "sectacms/pages/web_page.html"


class EventPage(sectaEventPage):
    class Meta:
        verbose_name = "Event Page"

    parent_page_types = ["testapp.EventIndexPage"]
    subpage_types = []
    template = "sectacms/pages/event_page.html"


class EventIndexPage(sectaEventIndexPage):
    class Meta:
        verbose_name = "Events Landing Page"

    index_query_pagemodel = "testapp.EventPage"
    index_order_by_default = ""

    # Only allow EventPages beneath this page.
    subpage_types = ["testapp.EventPage"]

    template = "sectacms/pages/event_index_page.html"


class EventOccurrence(sectaEventOccurrence):
    event = ParentalKey(EventPage, related_name="occurrences")


class LocationPage(sectaLocationPage):
    class Meta:
        verbose_name = "Location Page"

    template = "sectacms/pages/location_page.html"

    # Only allow LocationIndexPages above this page.
    parent_page_types = ["testapp.LocationIndexPage"]


class LocationIndexPage(sectaLocationIndexPage):
    class Meta:
        verbose_name = "Location Landing Page"

    # Override to specify custom index ordering choice/default.
    index_query_pagemodel = "testapp.LocationPage"

    # Only allow LocationPages beneath this page.
    subpage_types = ["testapp.LocationPage"]

    template = "sectacms/pages/location_index_page.html"


class StreamFormPage(sectaStreamFormPage):
    class Meta:
        verbose_name = "Stream Form"

    template = "sectacms/pages/stream_form_page.html"


class StreamFormConfirmEmail(sectaEmail):
    page = ParentalKey("StreamFormPage", related_name="confirmation_emails")


"""
--------------------------------------------------------------------------------
CUSTOM PAGE TYPES for testing specific features. These should be based on
sectaPage when testing sectaPage-specific functionality (which is where most
of our logic lives).
--------------------------------------------------------------------------------
"""


class IndexTestPage(sectaPage):
    """
    Tests indexing features (show/sort/filter child pages).
    """

    class Meta:
        verbose_name = "Index Test Page"

    index_query_pagemodel = "testapp.WebPage"

    template = "sectacms/pages/base.html"

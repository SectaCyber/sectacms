"""
Create or customize your page models here.
"""

from sectacms.forms import sectaFormField
from sectacms.models import sectaArticleIndexPage
from sectacms.models import sectaArticlePage
from sectacms.models import sectaEmail
from sectacms.models import sectaEventIndexPage
from sectacms.models import sectaEventOccurrence
from sectacms.models import sectaEventPage
from sectacms.models import sectaFormPage
from sectacms.models import sectaLocationIndexPage
from sectacms.models import sectaLocationPage
from sectacms.models import sectaWebPage
from modelcluster.fields import ParentalKey


class ArticlePage(sectaArticlePage):
    """
    Article, suitable for news or blog content.
    """

    class Meta:
        verbose_name = "Article"
        ordering = ["-first_published_at"]

    # Only allow this page to be created beneath an ArticleIndexPage.
    parent_page_types = ["website.ArticleIndexPage"]

    template = "sectacms/pages/article_page.html"
    search_template = "sectacms/pages/article_page.search.html"


class ArticleIndexPage(sectaArticleIndexPage):
    """
    Shows a list of article sub-pages.
    """

    class Meta:
        verbose_name = "Article Landing Page"

    # Override to specify custom index ordering choice/default.
    index_query_pagemodel = "website.ArticlePage"

    # Only allow ArticlePages beneath this page.
    subpage_types = ["website.ArticlePage"]

    template = "sectacms/pages/article_index_page.html"


class EventPage(sectaEventPage):
    class Meta:
        verbose_name = "Event Page"

    parent_page_types = ["website.EventIndexPage"]
    template = "sectacms/pages/event_page.html"


class EventIndexPage(sectaEventIndexPage):
    """
    Shows a list of event sub-pages.
    """

    class Meta:
        verbose_name = "Events Landing Page"

    index_query_pagemodel = "website.EventPage"

    # Only allow EventPages beneath this page.
    subpage_types = ["website.EventPage"]

    template = "sectacms/pages/event_index_page.html"


class EventOccurrence(sectaEventOccurrence):
    event = ParentalKey(EventPage, related_name="occurrences")


class FormPage(sectaFormPage):
    """
    A page with an html <form>.
    """

    class Meta:
        verbose_name = "Form"

    template = "sectacms/pages/form_page.html"


class FormPageField(sectaFormField):
    """
    A field that links to a FormPage.
    """

    class Meta:
        ordering = ["sort_order"]

    page = ParentalKey("FormPage", related_name="form_fields")


class FormConfirmEmail(sectaEmail):
    """
    Sends a confirmation email after submitting a FormPage.
    """

    page = ParentalKey("FormPage", related_name="confirmation_emails")


class LocationPage(sectaLocationPage):
    """
    A page that holds a location.  This could be a store, a restaurant, etc.
    """

    class Meta:
        verbose_name = "Location Page"

    template = "sectacms/pages/location_page.html"

    # Only allow LocationIndexPages above this page.
    parent_page_types = ["website.LocationIndexPage"]


class LocationIndexPage(sectaLocationIndexPage):
    """
    A page that holds a list of locations and displays them with a Google Map.
    This does require a Google Maps API Key in Settings > Secta Settings
    """

    class Meta:
        verbose_name = "Location Landing Page"

    # Override to specify custom index ordering choice/default.
    index_query_pagemodel = "website.LocationPage"

    # Only allow LocationPages beneath this page.
    subpage_types = ["website.LocationPage"]

    template = "sectacms/pages/location_index_page.html"


class WebPage(sectaWebPage):
    """
    General use page with featureful streamfield and SEO attributes.
    """

    class Meta:
        verbose_name = "Web Page"

    template = "sectacms/pages/web_page.html"

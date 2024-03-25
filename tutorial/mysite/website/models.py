"""
Create or customize your page models here.
"""

from modelcluster.fields import ParentalKey
from sectacms.forms import sectaFormField
from sectacms.models import (
    sectaArticlePage,
    sectaArticleIndexPage,
    sectaEmail,
    sectaFormPage,
    sectaWebPage,
)
from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField
from wagtail.images import get_image_model_string


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


class WebPage(sectaWebPage):
    """
    General use page with featureful streamfield and SEO attributes.
    Template renders all Navbar and Footer snippets in existence.
    """

    class Meta:
        verbose_name = "Web Page"

    template = "sectacms/pages/web_page.html"


class CupcakesIndexPage(sectaWebPage):
    """
    Landing page for Cupcakes
    """

    class Meta:
        verbose_name = "Cupcakes Landing Page"

    # Override to specify custom index ordering choice/default.
    index_query_pagemodel = "website.CupcakesPage"

    # Only allow CupcakesPages beneath this page.
    subpage_types = ["website.CupcakesPage"]

    template = "website/pages/cupcakes_index_page.html"


class CupcakesPage(sectaWebPage):
    """
    Custom page for individual cupcakes
    """

    class Meta:
        verbose_name = "Cupcakes Page"

    # Only allow this page to be created beneath an CupcakesIndexPage.
    parent_page_types = ["website.CupcakesIndexPage"]

    template = "website/pages/cupcakes_page.html"

    # The name of the cucpake will be in the page title
    description = RichTextField(
        verbose_name="Cupcake Description", null=True, blank=True, default=""
    )
    photo = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Cupcake Photo",
    )
    DAYS_CHOICES = (
        ("Weekends Only", "Weekends Only"),
        ("Monday-Friday", "Monday-Friday"),
        ("Tuesday/Thursday", "Tuesday/Thursday"),
        ("Seasonal", "Seasonal"),
    )
    days_available = models.CharField(
        choices=DAYS_CHOICES, max_length=20, default=""
    )

    # Add custom fields to the body
    body_content_panels = sectaWebPage.body_content_panels + [
        FieldPanel("description"),
        FieldPanel("photo"),
        FieldPanel("days_available"),
    ]

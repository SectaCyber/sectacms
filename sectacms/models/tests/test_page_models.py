from datetime import timedelta
from django.test import Client
from django.utils import timezone
from wagtail.test.utils import WagtailPageTests

from sectacms.models.page_models import (
    sectaArticleIndexPage,
    sectaArticlePage,
    sectaEventIndexPage,
    sectaEventPage,
    sectaFormPage,
    sectaLocationIndexPage,
    sectaLocationPage,
    sectaPage,
    sectaStreamFormPage,
    sectaWebPage,
    get_page_models,
)
from sectacms.models.snippet_models import Classifier, ClassifierTerm
from sectacms.tests.testapp.models import (
    ArticleIndexPage,
    ArticlePage,
    EventIndexPage,
    EventPage,
    EventOccurrence,
    FormPage,
    IndexTestPage,
    LocationIndexPage,
    LocationPage,
    StreamFormPage,
    WebPage,
)


class BasicPageTestCase:
    """
    This is a testing mixin used to run common tests for basic versions of page types.
    """

    class Meta:
        abstract = True

    def setUp(self):
        self.client = Client()
        self.basic_page = self.model(title=str(self.model._meta.verbose_name))
        self.homepage = WebPage.objects.get(url_path="/home/")
        self.homepage.add_child(instance=self.basic_page)

    def tearDown(self):
        self.basic_page.delete()

    def test_get(self):
        """
        Tests to make sure a basic version of the page serves a 200 from a GET request.
        """
        response = self.client.get(self.basic_page.url, follow=True)
        self.assertEqual(response.status_code, 200)


class AbstractPageTestCase:
    """
    This is a testing mixin used to run common tests for abstract page types.
    """

    class Meta:
        abstract = True

    def test_not_available(self):
        """
        Tests to make sure the page is not creatable and not in our global
        list of page models.
        """
        self.assertFalse(self.model.is_creatable)
        self.assertFalse(self.model in get_page_models())


class ConcretePageTestCase:
    """
    This is a testing mixin used to run common tests for concrete page types.
    """

    class Meta:
        abstract = True

    def test_is_available(self):
        """
        Tests to make sure the page is creatable and in our global list of
        page models.
        """
        self.assertTrue(self.model.is_creatable)
        self.assertTrue(self.model in get_page_models())


class ConcreteBasicPageTestCase(ConcretePageTestCase, BasicPageTestCase):
    class Meta:
        abstract = True


class ConcreteFormPageTestCase(ConcreteBasicPageTestCase):
    class Meta:
        abstract = True

    def test_post(self):
        """
        Tests to make sure a basic version of the page accepts data and is
        viewable in the Wagtail admin.
        """
        # TODO: add form field via streamfield.
        response = self.client.post(
            self.basic_page.url, {"name": "Monty Python"}, follow=True
        )
        self.assertEqual(response.status_code, 200)
        # TODO: log in as superuser and get wagtail admin form submission page.

    def test_spam(self):
        """
        Test to check if the default spam catching works.
        """
        response = self.client.post(
            self.basic_page.url,
            {"cr-decoy-comments": "This is Spam"},
            follow=True,
        )
        messages = list(response.context["messages"])
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), self.basic_page.get_spam_message())

    def test_not_spam(self):
        """
        Test to check if the default spam catching won't mark correct posts as spam.
        """
        response = self.client.post(self.basic_page.url)
        self.assertFalse(hasattr(response, "is_spam"))


class sectaArticleIndexPageTestCase(AbstractPageTestCase, WagtailPageTests):
    model = sectaArticleIndexPage


class sectaArticlePageTestCase(AbstractPageTestCase, WagtailPageTests):
    model = sectaArticlePage


class sectaFormPageTestCase(AbstractPageTestCase, WagtailPageTests):
    model = sectaFormPage


class sectaPageTestCase(WagtailPageTests):
    model = sectaPage

    def test_not_available(self):
        self.assertFalse(self.model.is_creatable)
        self.assertTrue(self.model in get_page_models())


class sectaWebPageTestCase(AbstractPageTestCase, WagtailPageTests):
    model = sectaWebPage


class sectaLocationIndexPageTestCase(AbstractPageTestCase, WagtailPageTests):
    model = sectaLocationIndexPage


class sectaLocationPageTestCase(AbstractPageTestCase, WagtailPageTests):
    model = sectaLocationPage


class sectaEventIndexPageTestCase(AbstractPageTestCase, WagtailPageTests):
    model = sectaEventIndexPage


class sectaEventPageTestCase(AbstractPageTestCase, WagtailPageTests):
    model = sectaEventPage


class sectaStreamFormPageTestCase(AbstractPageTestCase, WagtailPageTests):
    model = sectaStreamFormPage


# -- CONCRETE PAGES ------------------------------------------------------------


class ArticlePageTestCase(ConcreteBasicPageTestCase, WagtailPageTests):
    model = ArticlePage


class ArticleIndexPageTestCase(ConcreteBasicPageTestCase, WagtailPageTests):
    model = ArticleIndexPage


class FormPageTestCase(ConcreteFormPageTestCase, WagtailPageTests):
    model = FormPage


class WebPageTestCase(ConcreteBasicPageTestCase, WagtailPageTests):
    model = WebPage


class EventIndexPageTestCase(ConcreteBasicPageTestCase, WagtailPageTests):
    model = EventIndexPage


class EventPageTestCase(ConcreteBasicPageTestCase, WagtailPageTests):
    model = EventPage

    def setUp(self):
        super().setUp()
        self.occurrence = EventOccurrence(
            start=timezone.now(),
            end=timezone.now() + timedelta(days=1),
            event=self.basic_page,
        )
        self.occurrence.save()

    def tearDown(self) -> None:
        super().tearDown()
        self.occurrence.delete()


class LocationIndexPageTestCase(ConcreteBasicPageTestCase, WagtailPageTests):
    model = LocationIndexPage


class LocationPageTestCase(ConcreteBasicPageTestCase, WagtailPageTests):
    model = LocationPage


class StreamFormPageTestCase(ConcreteFormPageTestCase, WagtailPageTests):
    model = StreamFormPage


# -- PAGES FOR TESTING SPECIFIC FUNCTIONALITY ----------------------------------


class IndexTestCase(ConcreteBasicPageTestCase, WagtailPageTests):
    """
    Tests indexing features (show/sort/filter child pages).
    """

    model = IndexTestPage

    def setUp(self):
        super().setUp()

        # Create some child pages under this page.
        self.child_1 = WebPage(title=f"{self.basic_page.title} - Child 1")
        self.basic_page.add_child(instance=self.child_1)
        self.child_2 = WebPage(title=f"{self.basic_page.title} - Child 2")
        self.basic_page.add_child(instance=self.child_2)
        self.child_3 = WebPage(title=f"{self.basic_page.title} - Child 3")
        self.basic_page.add_child(instance=self.child_3)

        # Create some classifier terms for general purpose use.
        self.classifier = Classifier.objects.create(name="Classifier")
        self.term_a = ClassifierTerm.objects.create(
            classifier=self.classifier,
            name="Term A",
            sort_order=0,
        )
        self.term_b = ClassifierTerm.objects.create(
            classifier=self.classifier,
            name="Term B",
            sort_order=1,
        )

    def tearDown(self):
        super().tearDown()
        self.classifier.delete()

    def test_get_index_children(self):
        """
        Tests to make sure `get_index_children()` returns the correct queryset
        based on selected page settings.
        """
        # Test it without setting any options, ensure it is not broken.
        children = self.basic_page.get_index_children()
        self.assertIn(self.child_1, children)
        self.assertIn(self.child_2, children)
        self.assertIn(self.child_3, children)

        # Test index_order_by returns in the correct order.
        self.basic_page.index_order_by = "title"
        self.basic_page.save()
        children = self.basic_page.get_index_children()
        self.assertEqual(self.child_1, children[0])
        self.assertEqual(self.child_2, children[1])
        self.assertEqual(self.child_3, children[2])

        # Test index_order_by classifier returns in the correct order.
        self.basic_page.index_order_by_classifier = self.classifier
        self.basic_page.index_order_by = "title"
        self.basic_page.save()
        self.child_3.classifier_terms.add(self.term_a)
        self.child_3.save()
        self.child_1.classifier_terms.add(self.term_b)
        self.child_1.save()
        self.child_2.classifier_terms.add(self.term_b)
        self.child_2.save()
        children = self.basic_page.get_index_children()
        self.assertEqual(self.child_3, children[0])
        self.assertEqual(self.child_1, children[1])
        self.assertEqual(self.child_2, children[2])

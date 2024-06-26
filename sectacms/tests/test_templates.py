import pytest
from django.contrib.auth import get_user_model
from django.test import override_settings, TestCase


EXPECTED_BANNER_HTML = """
<div class="Secta-banner" style="background-color:#ff0; color:#000; text-align:center; padding:4px;">
  Test
</div>
"""


@pytest.mark.django_db
class TestSiteBanner(TestCase):
    @override_settings(Secta_BANNER="Test")
    def test_with_banner(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertInHTML(
            EXPECTED_BANNER_HTML, response.content.decode("utf-8")
        )

    def test_without_banner(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertNotIn("secta-banner", response.content.decode("utf-8"))


@pytest.mark.django_db
class TestWagtailAdminBanner(TestCase):
    def setUp(self):
        admin = get_user_model().objects.create_superuser(
            "admin", email="admin@example.com", password="admin"
        )
        self.client.force_login(admin)

    def tearDown(self):
        self.client.logout()

    @override_settings(Secta_BANNER="Test")
    def test_with_banner(self):
        response = self.client.get("/admin/")
        self.assertEqual(response.status_code, 200)
        self.assertInHTML(
            EXPECTED_BANNER_HTML, response.content.decode("utf-8")
        )

    def test_without_banner(self):
        response = self.client.get("/admin/")
        self.assertEqual(response.status_code, 200)
        self.assertNotIn("secta-banner", response.content.decode("utf-8"))

from django.urls import include, path, re_path
from django.contrib import admin
from wagtail.documents import urls as wagtaildocs_urls
from sectacms import admin_urls as Secta_admin_urls
from sectacms import search_urls as Secta_search_urls
from sectacms import urls as Secta_urls

urlpatterns = [
    path("django-admin/", admin.site.urls),
    path("admin/", include(Secta_admin_urls)),
    path("docs/", include(wagtaildocs_urls)),
    path("search/", include(Secta_search_urls)),
    re_path(r"", include(Secta_urls)),
]

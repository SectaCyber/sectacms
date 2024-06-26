from django.conf import settings
from django.urls import include, path, re_path
from django.contrib import admin
from wagtail.documents import urls as wagtaildocs_urls
from sectacms import admin_urls as Secta_admin_urls
from sectacms import search_urls as Secta_search_urls
from sectacms import urls as Secta_urls

urlpatterns = [
    # Admin
    path("django-admin/", admin.site.urls),
    path("admin/", include(Secta_admin_urls)),
    # Documents
    path("docs/", include(wagtaildocs_urls)),
    # Search
    path("search/", include(Secta_search_urls)),
    # For anything not caught by a more specific rule above, hand over to
    # the page serving mechanism. This should be the last pattern in
    # the list:
    re_path(r"", include(Secta_urls)),
    # Alternatively, if you want pages to be served from a subpath
    # of your site, rather than the site root:
    #    re_path(r"^pages/", include(Secta_urls)),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

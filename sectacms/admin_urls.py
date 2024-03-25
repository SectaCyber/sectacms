from django.urls import include, path
from wagtail.admin import urls as wagtailadmin_urls
from sectacms.views import import_index, import_pages_from_csv_file


urlpatterns = [
    path(
        "secta/import-export/",
        import_index,
        name="import_index",
    ),
    path(
        "secta/import-export/import_from_csv/",
        import_pages_from_csv_file,
        name="import_from_csv",
    ),
    path(
        "",
        include(wagtailadmin_urls),
    ),
]

from django.apps import AppConfig


class sectacmsConfig(AppConfig):
    name = "sectacms"
    verbose_name = "Wagtail Secta"
    # TODO: At some point in the future, change this to BigAutoField and create
    # the corresponding migration for concrete models in sectacms.
    default_auto_field = "django.db.models.AutoField"

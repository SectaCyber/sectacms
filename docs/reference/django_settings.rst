Wagtail Secta Django Settings
===========================

Default settings are loaded from ``sectacms/settings.py``. Available settings
for Wagtail Secta:


Secta_BANNER
----------

If you define a value for this ``Secta_BANNER``, sectaCMS will show this text in
a banner on both the front end and in the CMS of your site. This is useful for
flagging non-production environments like staging. For example::

    Secta_BANNER = "Staging Environment. Production is over here: <a href='https://example.com'>Example link</a>."

You can include basic HTML code, such as a link, in the banner.

The banner defaults to yellow background and black text. If you want to
customize the color, you can specify any HTML color name or code. For example::

    Secta_BANNER_BACKGROUND = '#FFFFE0'	# light yellow background
    Secta_BANNER_TEXT_COLOR = '#000'		# black text color

For greater customization, you can fully override the banner's HTML template:
``sectacms/includes/Secta_banner.html``.


Secta_BANNER_BACKGROUND
---------------------

String of a valid CSS color code to change the background of the banner.


Secta_BANNER_TEXT_COLOR
---------------------

String of a valid CSS color code to change the text color of the banner.


Secta_FRONTEND_*
--------------

Various frontend settings to specify defaults and choices used in the wagtail
admin related to rendering blocks, pages, and templates. By default, all
Secta_FRONTEND_* settings are designed to work with Bootstrap 5 CSS framework, but
these can be customized if using a different CSS framework or theme variant.

`Available settings are defined here <https://github.com/SectaCyber/sectacms/blob/main/sectacms/settings.py>`.


Secta_PROTECTED_MEDIA_ROOT
------------------------

The directory where files from File Upload fields on Form Pages are saved. These
files are served through Django using ``Secta_PROTECTED_MEDIA_URL`` and require
login to access. Defaults to ``protected/`` in your project directory.


Secta_PROTECTED_MEDIA_UPLOAD_WHITELIST
------------------------------------

The allowed filetypes for media upload in the form of a list of file type
extensions. Default is blank. For example, to only allow documents and images,
set to: ``['.pdf', '.doc', '.docx', '.txt', '.rtf', '.jpg', '.jpeg', '.png',
'.gif']``


Secta_PROTECTED_MEDIA_UPLOAD_BLACKLIST
------------------------------------

The disallowed filetypes for media upload in the form of a list of file type
extensions. Defaults to ``['.sh', '.exe', '.bat', '.ps1', '.app', '.jar', '.py',
'.php', '.pl', '.rb']``


Secta_PROTECTED_MEDIA_URL
-----------------------

The URL for protected media files from form file uploads. Defaults to
``'/protected/'``

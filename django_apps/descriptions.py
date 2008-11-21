import re
from django.utils.translation import ugettext_lazy as _

_apps_descriptions = [
    (r'.*django_dzenlog',               _('Abstract blogging application.')),
    (r'.*django_markdown2',             _('Markdown2 filter tag.')),
    (r'.*dzenlog_text',                 _('Text posts for blog (based on django_dzenlog).')),
    (r'.*dzenlog_link',                 _('Link posts for blog (based on django_dzenlog).')),
    (r'.*tagging',                      _('General tagging apllication.')),
    (r'.*django_faces',                 _('Pavatar, gravatar and favicons based avatars.')),
    (r'.*django_apps',                  _('Shows the installed application, their versions and descriptions.')),
    (r'.*pagination',                   _('Limits number of entries per page.')),
    (r'.*threadedcomments',             _('Flexible threaded commenting system.')),
    (r'.*dbtemplates',                  _('Editable templates, stored in the database.')),
    (r'.*django_openid',                _('OpenID server and consumer.')),
    (r'.*django_freetext',              _('Editable pieces of the content.')),
    (r'.*compress',                     _('Javascript and CSS compressor.')),
    (r'.*utils',                        _('Misc stuff.')),
    (r'.*django_extensions',            _('Global custom management extensions.')),
    (r'.*basic.inlines',                _('Inline markup to insert content objects into other pieces of content.')),
    (r'.*basic.media',                  _('Audio, video and images.')),
    (r'.*django.contrib.auth',          _('Django\'s authentication framework.')),
    (r'.*django.contrib.contenttypes',  _('Framework for hooking into "types" of content.')),
    (r'.*django.contrib.sessions',      _('Sessions support.')),
    (r'.*django.contrib.sites',         _('Multi-site support.')),
    (r'.*django.contrib.admin',         _('The automatic Django administrative interface.')),
    (r'.*django.contrib.humanize',      _('Template filters for adding a "human touch" to data.')),
    (r'.*django.contrib.flatpages',     _('Framework for managing simple "flat" HTML content in a database.')),
    (r'.*django.contrib.sitemaps',      _('A framework for generating Google sitemap XML files.')),
    (r'.*django.contrib.webdesign',     _('Helpers and utilities for Web designers.')),
]

def get_description(app_name):
    for pattern, description in _apps_descriptions:
        if re.match(pattern, app_name) is not None:
            return description
    return ''


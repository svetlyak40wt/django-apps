import re
from django import template
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from django_apps.descriptions import get_description

register = template.Library()

class InstalledAppsNode(template.Node):
    def __init__(self, var_name):
        self.var_name = var_name

    def render(self, context):
        def get_info(module_name):
            mod = __import__(module_name)
            version = getattr(mod, '__version__',
                      getattr(mod, 'VERSION', _('unknown')))
            if isinstance(version, (tuple, list)):
                version = '.'.join(map(str, version))
            return dict(name = module_name,
                        version = version,
                        description = get_description(module_name))

        try:
            context[self.var_name] = [get_info(mod) for mod in settings.INSTALLED_APPS]
        except Exception, e:
            context[self.var_name] = e
        print context[self.var_name]
        return ''

def installed_apps(parser, token):
    try:
        tag_name, arg = token.contents.split(None, 1)
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires arguments" % token.contents.split()[0]
    m = re.search(r'as (\w+)', arg)
    if not m:
        raise template.TemplateSyntaxError, "%r tag had invalid arguments" % tag_name
    var_name = m.groups()[0]
    return InstalledAppsNode(var_name)

register.tag(installed_apps)


from django import template
from wagtail.core.models import Site

from wagtail_favicon.models import FaviconSettings
from wagtail_favicon.utils import get_rendition_url

register = template.Library()


@register.inclusion_tag('tags/favicon_meta.html', takes_context=True)
def favicon_meta(context):
    site = Site.find_for_request(context.get('request'))
    favicon_settings = FaviconSettings.for_site(site)
    icon_image = favicon_settings.base_favicon_image
    ms_image = get_rendition_url(icon_image, 'fill-144x144') if icon_image else None

    return {
        'icon_image': icon_image,
        'theme_color': favicon_settings.app_theme_color,
        'apple_icons': favicon_settings.apple_icons,
        'icons': favicon_settings.icons,
        'ms_image': ms_image,
    }

from django.template.response import TemplateResponse
from django.http import JsonResponse, Http404
from wagtail.core.models import Site

from .models import FaviconSettings


def browser_config(request):
    settings = FaviconSettings.for_site(Site.find_for_request(request))
    image = settings.base_favicon_image

    if image is None:
        raise Http404

    return TemplateResponse(
        request,
        'browser-config.xml',
        {
            'request': request,
            'app_theme_color': settings.app_theme_color,
            'icon_70': image.get_rendition('fill-70x70').url,
            'icon_150': image.get_rendition('fill-150x150').url,
            'icon_310': image.get_rendition('fill-310x310').url,
        },
        content_type='application/xml'
    )


def icon_manifest(request):
    settings = FaviconSettings.for_site(Site.find_for_request(request))
    image = settings.base_favicon_image

    if image is None:
        raise Http404

    content = {
        'icons': [
            {
                "src": image.get_rendition('fill-36x36').url,
                "sizes": "36x36",
                "type": "image/png",
                "density": "0.75"
            }, {
                "src": image.get_rendition('fill-48x48').url,
                "sizes": "48x48",
                "type": "image/png",
                "density": "1.0"
            }, {
                "src": image.get_rendition('fill-72x72').url,
                "sizes": "72x72",
                "type": "image/png",
                "density": "1.5"
            }, {
                "src": image.get_rendition('fill-96x96').url,
                "sizes": "96x96",
                "type": "image/png",
                "density": "2.0"
            }, {
                "src": image.get_rendition('fill-144x144').url,
                "sizes": "144x144",
                "type": "image/png",
                "density": "3.0"
            }, {
                "src": image.get_rendition('fill-192x192').url,
                "sizes": "192x192",
                "type": "image/png",
                "density": "4.0"
            }
        ]
    }

    if settings.app_name:
        content['name'] = settings.app_name

    if settings.app_theme_color:
        content['theme_color'] = settings.app_theme_color

    return JsonResponse(content)


from django.http import JsonResponse, Http404
from django.template.response import TemplateResponse

from wagtail.models import Site

from .models import FaviconSettings
from .utils import get_rendition_url


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
            'icon_70': get_rendition_url(image, 'fill-70x70'),
            'icon_150': get_rendition_url(image, 'fill-150x150'),
            'icon_310': get_rendition_url(image, 'fill-310x310'),
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
                "src": get_rendition_url(image, 'fill-36x36'),
                "sizes": "36x36",
                "type": "image/png",
                "density": "0.75"
            }, {
                "src": get_rendition_url(image, 'fill-48x48'),
                "sizes": "48x48",
                "type": "image/png",
                "density": "1.0"
            }, {
                "src": get_rendition_url(image, 'fill-72x72'),
                "sizes": "72x72",
                "type": "image/png",
                "density": "1.5"
            }, {
                "src": get_rendition_url(image, 'fill-96x96'),
                "sizes": "96x96",
                "type": "image/png",
                "density": "2.0"
            }, {
                "src": get_rendition_url(image, 'fill-144x144'),
                "sizes": "144x144",
                "type": "image/png",
                "density": "3.0"
            }, {
                "src": get_rendition_url(image, 'fill-192x192'),
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

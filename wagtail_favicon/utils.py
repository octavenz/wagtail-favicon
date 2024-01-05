from wagtail.images.views.serve import generate_image_url
from django.urls import NoReverseMatch


def get_rendition_url(image, filter_spec):
    """
    Efficiently get the URL for a rendition.

    If enabled, will attempt to use the image serve view before retrieving the rendition URL directly.
    https://docs.wagtail.org/en/stable/advanced_topics/images/image_serve_view.html
    """
    try:
        return generate_image_url(image, filter_spec)
    except NoReverseMatch:
        # Serve view isn't available, fall back to direct URL
        return image.get_rendition(filter_spec).url

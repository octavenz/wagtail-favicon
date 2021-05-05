from django.db import models
from django.utils.functional import cached_property

from wagtail.admin.edit_handlers import MultiFieldPanel, FieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.images import get_image_model_string
from wagtail.images.edit_handlers import ImageChooserPanel

from .validators import validate_hex


class FaviconRenditions:
    icon_sizes = [
        '192x192',
        '96x96',
        '32x32',
        '16x16',
    ]

    apple_icon_sizes = [
        '180x180',
        '152x152',
        '144x144',
        '120x120',
        '114x114',
        '76x76',
        '72x72',
        '60x60',
        '57x57',
    ]

    def get_rendition(self, size):
        image = self.base_favicon_image
        rendition = image.get_rendition(f'fill-{size}')
        return rendition.url

    def make_renditions(self, sizes):
        if self.base_favicon_image is None:
            return []

        return [
            {
                'size': size,
                'url': self.get_rendition(size)
            } for size in sizes
        ]

    @cached_property
    def icons(self):
        return self.make_renditions(self.icon_sizes)

    @cached_property
    def apple_icons(self):
        return self.make_renditions(self.apple_icon_sizes)


@register_setting
class FaviconSettings(BaseSetting, FaviconRenditions):
    base_favicon_image = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    app_theme_color = models.CharField(
        max_length=7,
        blank=True,
        help_text='Hex colour value',
        validators=(validate_hex,)
    )

    app_name = models.CharField(
        max_length=128,
        blank=True,
        help_text='App name for manifest.json'
    )

    panels = [
        MultiFieldPanel(
            [
                FieldPanel('app_name'),
                FieldPanel('app_theme_color'),
                ImageChooserPanel('base_favicon_image'),
            ],
            heading="Favicon Settings",
            classname="collapsible"
        ),
    ]

    class Meta:
        verbose_name = 'Favicon'



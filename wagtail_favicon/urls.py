from django.urls import path
from .views import browser_config, icon_manifest, FaviconView

urls = [
    path('browser-config.xml', browser_config),
    path('manifest.json', icon_manifest),
    path('favicon.ico', FaviconView.as_view())
]

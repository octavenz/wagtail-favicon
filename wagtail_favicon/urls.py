from django.urls import path
from .views import browser_config, icon_manifest

urls = [
    path('browser-config.xml', browser_config),
    path('manifest.json', icon_manifest),
]

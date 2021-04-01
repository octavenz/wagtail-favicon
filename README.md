# Wagtail Favicon

Easily add shortcut icons to any wagtail site. Upload a .png image from a wagtail settings page and wagtail-favicon will resize it and add provide markup to your pages via a template tag.

---

### Installation & Setup

#### Install with pip

```
# todo: move to pypi
pip install -e git+https://github.com/octavenz/wagtail-favicon.git#egg=wagtail_favicon
```

#### Add to Django installed apps

```
INSTALLED_APPS = [
    #...
    'wagtail_favicon',
]
```

#### Add routes to app.urls

```
from wagtail_favicon.urls import urls as favicon_urls

urlpatterns += [
    url(r'^documents/', include(wagtaildocs_urls)),
    url(r'^search/$', search, name='search'),
    url(r'', include(wagtail_urls)),

    url(r'', include(favicon_urls)),  # <------ add urls to existing urls
]
```

Once you've completed setup you will now be able to access the folloing urls:
- https://example.com/manifest.json
- https://example.com/browser-config.xml


#### Add template tag to <head> tag in templates/base.html

```
{% load favicon_tags %}
  <html>
    <head>
        {% favicon_meta %}
    </head>
```


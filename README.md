# Wagtail Favicon

Easily add shortcut icons to any wagtail site. Upload a .png image from a wagtail settings page and wagtail-favicon will resize it and add provide markup to your pages via a template tag.

---

### Installation & Setup

#### Install with pip

```
pip install wagtail-favicon

or

poetry add wagtail-favicon
```

#### Add to Django installed apps

```
INSTALLED_APPS = [
    #...
    'wagtail.contrib.settings'  # <-- ensure you have wagtail settings loaded 
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

# note: newer versions of django may use `path` instead of `url`
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

#### Edit Settings

Go to `Wagtail Admin >> Settings >> Favicon`  

Configure settings  

For best results use a transparent png at 1024 x 1024.  
Ideally pre optimised with a tool like [tinypng.com](https://tinypng.com).

![Screenshot](https://github.com/octavenz/wagtail-favicon/blob/master/screenshot.jpg)


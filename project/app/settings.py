# coding=UTF-8
from __future__ import unicode_literals
from cubane.settings import default_env
import dj_database_url
import os


env = default_env(
    __name__,
    os.environ.get('DOMAIN_NAME', ''),
    os.environ.get('ADMIN_EMAIL', ''),
    csrf=True,
    ssl=False
)


#
# Site
#
SECRET_KEY = os.environ.get('SECRET_KEY', '')
ROOT_URLCONF = 'app.urls'


#
# Database
#
DATABASE_URL = os.environ.get('DATABASE_URL')
if DATABASE_URL:
    DATABASES = {
        'default': dj_database_url.config(default=DATABASE_URL)
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('POSTGRES_DB', ''),
            'USER': os.environ.get('POSTGRES_USER', ''),
            'PASSWORD': os.environ.get('POSTGRES_PASSWORD', ''),
            'HOST':  os.environ.get('POSTGRES_HOST', 'localhost'),
            'PORT': os.environ.get('POSTGRES_PORT', '5432'),
        }
    }


#
# Media/Static Paths
#
PUBLIC_HTML_ROOT = '/app/public'
STATICFILES_DIRS = (
    '/app/app/static',
)
MEDIA_ROOT = '/app/public/media'
STATIC_ROOT = '/app/public/static'
CUBANE_FONT_ROOT = '/app/public/media/fonts'
PREPEND_WWW = False


#
# Apps
#
env.add_apps([
    'cubane',
    'cubane.backend',
    'cubane.backend.accounts',
    'cubane.cms',
    'cubane.media',
    'cubane.medialoader',
    'cubane.enquiry',
    'cubane.cssreset',
    'cubane.svgicons',
    'cubane.fonts',
    'app',
])


#
# Resources
#
RESOURCES = {
    'frontend': [
        'cubane.cssreset',
        'cubane.legacy.jquery',
        'cubane.enquiry',
        'cubane.svgicons',
        'app',
    ],
    'inline': [
        'cubane.medialoader',
    ]
}


#
# Image Shapes
#
IMAGE_SHAPES = {
    # Add you own image shapes used by your website design, for example
    # header: '1600:800'.
    # The size given here is arbitary since it only defines an aspect
    # ratio and not particular pixel sizes. For example 1600:800 could
    # also be defined as 800:400, which is the same aspect ratio.
}


#
# Navigation
#
CMS_NAVIGATION = (
    ('header', 'Header'),
    ('footer', 'Footer'),
)


#
# CMS
#
CMS = 'app.views.APP_CMS'
CMS_TEMPLATES = (
    ('app/page.html', 'Page'),
    ('app/mail/enquiry_visitor.html', 'Enquiry Email'),
)
CMS_SLOTNAMES = [
    'content',
    'signature'
]
CMS_SETTINGS_MODEL = 'app.models.Settings'
CMS_PAGE_MODEL = 'app.models.CustomPage'
PAGE_HIERARCHY = False


#
# Enquiry
#
ENQUIRY_MODEL = 'app.models.Enquiry'
ENQUIRY_CLIENT_TEMPLATE = 'app/mail/enquiry_client.html'
CAPTCHA = 'new_recaptcha'
CAPTCHA_SITE_KEY = os.environ.get('CAPTCHA_SITE_KEY', '')
CAPTCHA_SECRET_KEY = os.environ.get('CAPTCHA_SECRET_KEY', '')


#
# Google Maps
#
CUBANE_GOOGLE_MAP_API_KEY = os.environ.get('CUBANE_GOOGLE_MAP_API_KEY', '')

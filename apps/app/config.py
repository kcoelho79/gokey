# -*- encoding: utf-8 -*

from django.apps import AppConfig

class MyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.app'
    label = 'apps_app'

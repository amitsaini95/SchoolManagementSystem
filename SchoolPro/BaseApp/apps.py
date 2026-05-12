from django.apps import AppConfig

class BaseappConfig(AppConfig):
    name = 'BaseApp'
    def ready(self):
        import BaseApp.signals
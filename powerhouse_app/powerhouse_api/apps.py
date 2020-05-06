from django.apps import AppConfig


class PowerhouseApiConfig(AppConfig):
    name = 'powerhouse_api'

    def ready(self):
        import powerhouse_api.signals

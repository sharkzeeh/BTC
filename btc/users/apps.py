from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    # IMPORT SIGNALS
    def ready(self):
        import users.signals
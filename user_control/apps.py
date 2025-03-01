from django.apps import AppConfig


class UserControlConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "user_control"

    def ready(self):
        from . import signals

        return super().ready()

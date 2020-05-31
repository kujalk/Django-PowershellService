from django.apps import AppConfig


class FirewallConfig(AppConfig):
    name = 'firewall'

    def ready(self):
        from updateservice import scheduler
        scheduler.start()
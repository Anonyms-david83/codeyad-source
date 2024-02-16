from django.apps import AppConfig


class TicketAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ticket_app'
    verbose_name = 'tickets' #the showed name in the models header

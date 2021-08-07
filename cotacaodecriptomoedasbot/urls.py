from django.urls import path
from .views import handle_bot_request, poll_updates, set_my_webhook

urlpatterns = [
    path('update/', handle_bot_request),
    path('poll/', poll_updates),
    path('set_webhook/', set_my_webhook)
]

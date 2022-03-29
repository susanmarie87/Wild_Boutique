from django.http import HttpResponse


class StripeWH_Handler:
    """Handles Stripe Webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handles unexpected webhook events
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)


    def handle_payment_intent_succeeded(self, event):
        """
        Handles unexpecteds webhook event
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

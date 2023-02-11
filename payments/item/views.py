from django.http import JsonResponse
from django.views.generic import TemplateView
from django.views import View
from django.conf import settings
import stripe
from .models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY


class ItemView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        item = Item.objects.get(id=self.kwargs['pk'])
        context = super(ItemView, self).get_context_data()
        context.update({
            'item': item,
            'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY
        })
        return context


class SuccessView(TemplateView):
    template_name = 'success.html'


class CancelView(TemplateView):
    template_name = 'cancel.html'


class StipeSessionId(View):

    def post(self, request, *args, **kwargs):
        item = Item.objects.get(id=self.kwargs['pk'])
        YOUR_DOMAIN = settings.YOUR_DOMAIN
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price_data': {
                        'currency': item.currency,
                        'unit_amount': item.price,
                        'product_data': {
                            'name': item.name,
                        }
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + 'app_item/success/',
            cancel_url=YOUR_DOMAIN + 'app_item/cancel/',
        )
        return JsonResponse({
            'id': checkout_session.id
        })

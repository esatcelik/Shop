import decimal

from shop.cart.cart_modifiers_base import BaseCartModifier

class Fixed7PercentTaxRate(BaseCartModifier):
    """
    This will add 7% of the subtotal of the order to the total.

    It is of course not very useful in the real world, but this is an
    example.
    """

    def get_extra_cart_price_field(self, cart, request):
        taxes = decimal.Decimal('0.07') * cart.subtotal_price
        to_append = ('Taxes total', taxes)
        return to_append
from decimal import Decimal
from django.conf import settings
from e_drugs.models import Medicine


class Cart(object):
    def __init__(self, request):
        """
        Initialize the cart.
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, medicine, quantity=1, override_quantity=False):
        """
        Add a medicine to the cart or update its quantity.
        """
        medicine_id = str(medicine.id)
        if medicine_id not in self.cart:
            self.cart[medicine_id] = {'quantity': 0, 'price': str(medicine.price_net)}
        if override_quantity:
            self.cart[medicine_id]['quantity'] = quantity
        else:
            self.cart[medicine_id]['quantity'] += quantity
        self.save()

    def save(self):
        # mark the session as "modified" to make sure it gets saved
        self.session.modified = True

    def remove(self, medicine):
        """
        Remove a medicine from the cart.
        """
        medicine_id = str(medicine.id)
        if medicine_id in self.cart:
            del self.cart[medicine_id]
            self.save()

    def __iter__(self):
        """
        Iterate over the items in the cart and get the medicines
        from the database.
        """
        medicine_ids = self.cart.keys()
        # get the product objects and add them to the cart
        medicines = Medicine.objects.filter(id__in=medicine_ids)

        cart = self.cart.copy()
        for medicine in medicines:
            cart[str(medicine.id)]['medicine'] = medicine

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
        Count all items in the cart.
        """
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        # remove cart from session
        del self.session[settings.CART_SESSION_ID]
        self.save()

from decimal import Decimal
from django.conf import settings
from pcmarket2.apps.products.models import Product


class Cart(object):
    def __init__(self, request):
        """
        ініціалізуєм корзину

        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # зберегти пусту корзину в сесії
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):
        """
        Добавити продукт в корзину або обновити його кількість.

        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart  # оновлення сесії cart
        self.session.modified = True  # відмітити сеанс як змінений

    def remove(self, product):
        """
        Видалення товару з корзини.

        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        """
        Перебор елементів корзини і получення продуктів із бази даних.
        """
        product_ids = self.cart.keys()
        products = Product.published.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
        Підрахунок всіх елементів корзини.
         """
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(
            Decimal(item['price']) * item['quantity']
            for item in self.cart.values()
         )

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()

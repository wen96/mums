from mumsapi import models


class CartSvc(object):
    """
        This class contains bussiness logic to calculate cart price.

        We assume cart price is an object like:
        [
            {
                'id': <product_id>
                'quantity': <product_quantity_in_pieces_or_gr>
            }
        ]
        The main method, we use to use, is calculate_cart_price, which returns the best price
        fitting with promotions and menus.
    """

    @classmethod
    def calculcate_cart_price(cls, cart):
        # We should check for each promition and each menu in case is coliding products, let the best price.
        # At the moment, we just coculate cart price without discounts.
        price = 0
        for cart_line in cart:
            product = models.Product.objects.get(pk=cart_line['id'])
            price += product.price * cart_line['quantity']
        return price

    @classmethod
    def calculate_promotion_discount(cls, cart):
        discount = 0
        for product_cart in cart:
            product = models.Product.objects.get(pk=product_cart['id'])
            discount += cls.calculate_price_discounts(product, product_cart['quantity'])
        return discount

    @classmethod
    def calculate_product_discount(cls, product, quantity):
        if not product.promition_set.is_empty() and quantity > 3:
            return (quantity // 3) * product.price
        else:
            return 0

    @classmethod
    def calculate_menus_discount(cls, cart):
        return 0

    @classmethod
    def calculate_menus(cls, products):
        menus = None
        for product in products:
            for menu in product.menus:
                if cls.is_menu_in_products(menu, products):
                    menus.append(menu)
        return menus

    @classmethod
    def calculate_best_menus(cls, cart):
        products = [models.Product.objects.get(pk=product_cart['id']) for product_cart in cart]
        menus = cls.calculate_menus(products)
        """ It calculates which menus combination get the better price
            This is too complex so, I let it to implement it in the future
            At the moment, we just return all menus
        """
        return menus

    @classmethod
    def is_menu_in_products(cls, menu, products):
        for product in menu.products:
            if product not in products:
                return False
        return True

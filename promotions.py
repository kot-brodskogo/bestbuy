from abc import ABC, abstractmethod


class Promotion(ABC):
    """ Abstract class for promotions. """
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity) -> float:
        """
        Applies the promotion to the given product and quantity.

        Args:
            product: The product instance.
            quantity: The quantity to apply the promotion to.

        Returns:
            float: The discounted price after applying the promotion.
        """
        pass


class SecondHalfPrice(Promotion):
    """ Represents a second item at half price promotion. """
    def apply_promotion(self, product, quantity) -> float:
        """
        Applies the second item at half price promotion.

        Args:
            product: The product instance.
            quantity: The quantity to apply the promotion to.

        Returns:
            float: The discounted price after applying the promotion.
        """
        half_price_items = quantity // 2
        full_price_items = quantity - half_price_items
        discounted_price = (full_price_items * product.price + half_price_items * product.price / 2)
        return discounted_price


class ThirdOneFree(Promotion):
    """ Represents a buy 2, get 1 free promotion. """

    def apply_promotion(self, product, quantity) -> float:
        """
        Applies the buy 2, get 1 free promotion.

        Args:
            product: The product instance.
            quantity: The quantity to apply the promotion to.

        Returns:
            float: The discounted price after applying the promotion.
        """
        free_items = quantity // 3
        full_price_items = quantity - free_items
        discounted_price = full_price_items * product.price
        return discounted_price


class PercentDiscount(Promotion):
    """ Represents a percentage discount promotion. """

    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity) -> float:
        """
        Applies the percentage discount promotion.

        Args:
            product: The product instance.
            quantity: The quantity to apply the promotion to.

        Returns:
            float: The discounted price after applying the promotion.
        """
        discounted_price = product.price * (1 - self.percent / 100)
        return discounted_price * quantity

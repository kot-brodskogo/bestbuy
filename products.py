from promotions import Promotion


class Product:
    """
        Represents a product in the store.

        Attributes:
            name (str): The name of the product.
            price (float): The price of the product.
            quantity (int): The quantity of the product in stock.
            active (bool): Whether the product is active or not.
        """
    def __init__(self, name, price, quantity):
        """
            Initializes a new Product instance.

            Raises:
                ValueError: If name is empty, or if price or quantity is negative.
            """
        if not name or price < 0 or quantity < 0:
            raise ValueError("Invalid input: name cannot be empty,"
                             "and price/quantity must be non-negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        self.promotion = None  # Initialize promotion to None

    def get_quantity(self) -> float:
        """
            Getter function for the quantity attribute.

            Returns:
                float: The quantity of the product.
            """
        return float(self.quantity)

    def set_quantity(self, new_quantity):
        """
            Setter function for the quantity attribute.

            Args:
                new_quantity: The new quantity value.

            Raises:
                ValueError: If new_quantity is negative.
            """
        if new_quantity < 0:
            raise ValueError("Quantity must be non-negative.")

        self.quantity = new_quantity

        # Deactivate the product if quantity reaches 0
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """
            Getter function for the active attribute.

            Returns:
                bool: True if the product is active, otherwise False.
            """
        return self.active

    def activate(self):
        """ Activates the product. """
        self.active = True

    def deactivate(self):
        """ Deactivates the product. """
        self.active = False

    def set_promotion(self, promotion: Promotion):
        """
        Sets the promotion for the product.

        Args:
            promotion: The promotion instance to set.
        """
        self.promotion = promotion

    def get_promotion(self) -> Promotion:
        """
        Gets the current promotion for the product.

        Returns:
            Promotion: The current promotion instance.
        """
        return self.promotion

    def show(self) -> str:
        """
            Returns a string representation of the product,
            including the current promotion if exists.

            Returns:
                str: A string representation of the product.
            """
        promotion_info = f", Promotion: {self.promotion.name}" if self.promotion else ""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}{promotion_info}"

    def buy(self, quantity) -> float:
        """
            Buys a given quantity of the product,
            applying the promotion if it exists.

            Args:
                quantity: The quantity to buy.

            Returns:
                float: The total price of the purchase.

            Raises:
                ValueError: If the product is not active, or if the quantity is invalid.
            """
        if not self.is_active():
            raise ValueError("Product is not active. Cannot make a purchase.")

        if quantity > self.quantity:
            raise ValueError("Invalid quantity for purchase.")

        if self.promotion:
            self.set_quantity(self.quantity - quantity)
            return self.promotion.apply_promotion(self, quantity)
        else:
            total_price = quantity * self.price
            self.set_quantity(self.quantity - quantity)
            return total_price


class NonStockedProduct(Product):
    """ Represents a non-stocked product in the store """
    def __init__(self, name, price):
        # Call the constructor of the parent class
        super().__init__(name, price, quantity=0)

    def show(self) -> str:
        """
        Overrides the show method to display the special characteristics of non-stocked products.

        Returns:
            str: A string representation of the non-stocked product.
        """
        promotion_info = f", Promotion: {self.promotion.name}" if self.promotion else ""
        return f"{self.name}, Price: {self.price}, Quantity: Not Applicable (Non-Stocked){promotion_info}"

    def buy(self, quantity) -> float:
        """
        Overrides the buy method to handle purchasing of a non-stocked product.

        Args:
            quantity: The quantity to buy.

        Returns:
            float: The total price of the purchase.
        """

        # For non-stocked products, quantity is not relevant; proceed with the purchase
        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)
        else:
            return self.price * quantity


class LimitedProduct(Product):
    """
    Represents a product with a limited purchase quantity in the store.

    Attributes:
        maximum (int): The maximum quantity allowed for purchase.
    """
    def __init__(self, name, price, quantity, maximum):
        """
        Initializes a new LimitedProduct instance.

        Args:
            name (str): The name of the product.
            price (float): The price of the product.
            quantity (int): The initial quantity of the product.
            maximum (int): The maximum quantity allowed for purchase.

        Raises:
            ValueError: If max_quantity is not a positive integer.
        """
        # Call the constructor of the parent class
        super().__init__(name, price, quantity)

        if not isinstance(maximum, int) or maximum <= 0:
            raise ValueError("max_quantity must be a positive integer.")

        self.maximum = maximum

    def show(self) -> str:
        """
        Overrides the show method to display the special characteristics of limited products.

        Returns:
            str: A string representation of the limited product.
        """
        promotion_info = f", Promotion: {self.promotion.name}" if self.promotion else ""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, " \
               f"Max Quantity: {self.maximum}{promotion_info}"

    def buy(self, quantity) -> float:
        """
        Overrides the buy method to handle limited purchase quantity.

        Args:
            quantity: The quantity to buy.

        Returns:
            float: The total price of the purchase.

        Raises:
            ValueError: If the quantity exceeds the maximum allowed quantity.
        """
        if quantity > self.maximum:
            raise ValueError(f"Quantity exceeds the maximum allowed quantity ({self.maximum}).")

        if self.promotion:
            self.set_quantity(self.quantity - quantity)
            return self.promotion.apply_promotion(self, quantity)
        else:
            return super().buy(quantity)

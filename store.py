from typing import List, Tuple
from products import Product


class Store:
    """
        Represents a store that manages a list of products.

        Attributes:
            products (List[Product]): The list of products in the store.
        """
    def __init__(self, products):
        """
            Initializes a new Store instance.

            Args:
                products (List[Product]): The initial list of products in the store.
            """
        self.products = products

    def add_product(self, product):
        """
            Adds a new product to the store.

            Args:
                product (Product): The product to add to the store.
            """
        self.products.append(product)

    def remove_product(self, product):
        """
            Removes a product from the store.

            Args:
                product (Product): The product to remove from the store.
            """
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self) -> int:
        """
            Calculates and returns the total quantity of all active products in the store.

            Returns:
                int: The total quantity in the store.
            """
        return sum(product.get_quantity() for product in self.products if product.is_active())

    def get_all_products(self) -> List[Product]:
        """
            Returns a list of all active products in the store.

            Returns:
                List[Product]: A list of all active products in the store.
            """
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        """
            Places an order for the products in the shopping list and returns the total cost.

            Args:
                shopping_list (List[Tuple[Product, int]]): The list of products
                and quantities to order.

            Returns:
                float: The total cost of the order.

            Raises:
                ValueError: If a product is not active or if the quantity in the order is invalid.
            """
        total_cost = 0.0

        for product, quantity in shopping_list:
            if product in self.products and product.is_active():
                if quantity > product.quantity:
                    raise ValueError(f"Not enough stock for {product.name}.")
                total_cost += product.buy(quantity)

        return total_cost

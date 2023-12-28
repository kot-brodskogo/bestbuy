from store import Store
import products


def show_menu():
    """ Displays the menu options for the user """
    print("Menu:")
    print("1. List all products in store")
    print("2. Show total amount in store")
    print("3. Make an order")
    print("4. Quit")


def list_all_products(store):
    """
        Lists all active products in the given store.

        Args:
            store (Store): The store object.
        """
    print("------")
    print("List of all products in store:")
    for index, product in enumerate(store.get_all_products(), start=1):
        print(f"{index}. {product.show()}")
    print("------")


def show_total_amount(store):
    """
        Displays the total quantity of all active products in the store.

        Args:
            store (Store): The store object.
        """
    total_quantity = store.get_total_quantity()
    print(f"Total quantity in store: {total_quantity}")


def make_order(store):
    """
        Takes user input to create a shopping list and place an order.

        Args:
            store (Store): The store object.
        """
    # Use a dictionary to store quantities for each product
    shopping_dict = {}

    list_all_products(store)
    print("When you want to finish order, enter empty text.")
    while True:
        try:
            product_index = input("Which product # do you want? ")
            if not product_index:
                break

            product_index = int(product_index)
            # Validate product index
            if 1 <= product_index <= len(store.products):
                product = store.products[product_index - 1]
            else:
                print("Invalid product number. Please try again.")
                continue

            quantity = int(input(f"Enter the quantity for {product.name}: "))

            # Validate quantity
            if quantity <= 0:
                print("Invalid quantity. Please enter a positive number.")
                continue

            # Accumulate quantities in the dictionary
            if product in shopping_dict:
                shopping_dict[product] += quantity
            else:
                shopping_dict[product] = quantity
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    try:
        # Convert the dictionary to a list of tuples for the order
        shopping_list = [(product, quantity) for product, quantity in shopping_dict.items()]
        # Place the order
        total_cost = store.order(shopping_list)

        # Display the total cost of the order
        print(f"Order placed successfully! Total cost: ${total_cost:.2f}")
    except ValueError as value_error:
        print(f"Error: {value_error}")


def start(store):
    """
        Entry point for the user interface.

        Args:
            store (Store): The store object.
        """
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            list_all_products(store)
        elif choice == '2':
            show_total_amount(store)
        elif choice == '3':
            make_order(store)
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


def main():
    """
        Initializes the store with an initial stock of products and starts the user interface.

        This function sets up an initial inventory of products for the store and then
        initiates the user interface by calling the `start` function.
        """
    # setup initial stock of inventory
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                    products.NonStockedProduct("Windows License", price=125),
                    products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
                    ]
    best_buy = Store(product_list)

    # Start the program
    start(best_buy)


if __name__ == "__main__":
    main()

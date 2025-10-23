import products, store


def start(store_object):
    while True:
        print("""
   Store Menu
   ----------
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
""")

        choice = input("Please choose a number: ")

        if choice == "1":
            print("--------------")
            for product in store_object.get_all_products():
                print(product.show())
            print("--------------")

        elif choice == "2":
            print(f"Total of {store_object.get_total_quantity()} items in store")

        elif choice == "3":
            print("------")
            for i, product in enumerate(store_object.get_all_products(), start=1):
                print(f"{i}. {product.show()}")
            print("------")
            print("When you want to finish order, enter empty text.")

            shopping_list = []

            while True:
                product_number = input("Which product # do you want? ")

                # If user enter an empty string: Close order
                if product_number == "":
                    break

                # Check for accepted number
                if not product_number.isdigit():
                    print("Please enter a valid number.")
                    continue

                product_number = int(product_number)

                # Check if product exists
                products = store_object.get_all_products()
                if product_number < 1 or product_number > len(products):
                    print("Invalid product number.")
                    continue

                amount = input("What amount do you want? ")
                if not amount.isdigit():
                    print("Please enter a valid quantity.")
                    continue

                amount = int(amount)

                shopping_list.append((products[product_number - 1], amount))
                print("Product added to list!\n")

            # Finish order
            if shopping_list:
                total = store_object.order(shopping_list)
                print("********")
                print(f"Order made! Total payment: ${total}")
                print("********")
            else:
                print("No products selected.")

        elif choice == "4":
            print("Goodbye!")
            break


def main():
    # setup initial stock of inventory
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250)
                    ]
    best_buy = store.Store(product_list)

    start(best_buy)


if __name__ == "__main__":
    main()
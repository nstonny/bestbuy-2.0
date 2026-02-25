from products import Product, NonStockedProduct, LimitedProduct
from store import Store

def show_menu():
    print("Store menu\n----------")
    menu_options = ["List all products in store", "Show total amount in store", "Make an order", "Quit"]
    for index, option in enumerate(menu_options, start=1):
        print(f"{index}. {option}")

def start(best_buy):
    show_menu()
    while True:
        try:
            user_selection = int(input("Please choose a number: "))
        except ValueError:
            print("Please enter a number")
            continue
        match user_selection:
            case 1:
                active_products = best_buy.get_all_products()
                for index, product in enumerate(active_products, start=1):
                    print(f"{index}.", end=" ")
                    print(product.show())
            case 2:
                print(f"\nTotal of {best_buy.get_total_quantity()} items in store")
            case 3:
                shopping_list= create_shopping_list(best_buy)
                print(f"********\nOrder made! Total payment: ${get_total_price(best_buy, shopping_list)}")
            case 4:
                break
            case _:
                print("Invalid option")

        print()
        input("Press enter to continue")
        show_menu()

def show_active_products(best_buy):
    print("------")
    for index, product in enumerate(best_buy.get_all_products(), start=1):
        print(f"{index}.", end=" ")
        print(product.show())
    print("------")

def create_shopping_list(best_buy):
    shopping_list = []
    show_active_products(best_buy)
    print("When you want to finish order, enter empty text.")
    user_product_selection = input("Which product # do you want? ")
    while user_product_selection != "":
        user_amount = int(input("What amount do you want? "))

        # add product and amount to shopping_list
        shopping_list.append((best_buy.get_all_products()[int(user_product_selection) -1], user_amount))
        print("Product added to list!")

        show_active_products(best_buy)
        print("When you want to finish order, enter empty text.")
        user_product_selection = input("Which product # do you want? ")

    return shopping_list

def get_total_price(best_buy, shopping_list):
    return best_buy.order(shopping_list)

def main():

    # setup initial stock of inventory
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250),
                    NonStockedProduct("Windows License", price=125),
                    LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
                    ]

    best_buy = Store(product_list)
    start(best_buy)

if __name__ == "__main__":
    main()
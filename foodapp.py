
class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

class Restaurant:
    def __init__(self, restaurant_id, name, menu):
        self.restaurant_id = restaurant_id
        self.name = name
        self.menu = menu 

class MenuItem:
    def __init__(self, item_id, name, price):
        self.item_id = item_id
        self.name = name
        self.price = price

class Order:
    def __init__(self, order_id, user, restaurant, items):
        self.order_id = order_id
        self.user = user
        self.restaurant = restaurant
        self.items = items  # List of MenuItem objects
        self.total_price = sum(item.price for item in items)


users = [
    User(user_id=1, name="Alice"),
    User(user_id=2, name="Bob")
]

restaurants = [
    Restaurant(
        restaurant_id=1,
        name="Pizza Place",
        menu=[
            MenuItem(item_id=1, name="Margherita", price=10),
            MenuItem(item_id=2, name="Pepperoni", price=12)
        ]
    ),
    Restaurant(
        restaurant_id=2,
        name="Food Palace",
        menu=[
            MenuItem(item_id=3, name="Indomie", price=8),
            MenuItem(item_id=4, name="Rice", price=7)
        ]
    )
]

orders = []

def list_restaurants():
    for restaurant in restaurants:
        print(f"{restaurant.restaurant_id}: {restaurant.name}")

def show_menu(restaurant_id):
    restaurant = next((r for r in restaurants if r.restaurant_id == restaurant_id), None)
    if restaurant:
        for item in restaurant.menu:
            print(f"{item.item_id}: {item.name} - ${item.price}")
    else:
        print("Restaurant not found.")

def place_order(user_id, restaurant_id, item_ids):
    user = next((u for u in users if u.user_id == user_id), None)
    restaurant = next((r for r in restaurants if r.restaurant_id == restaurant_id), None)
    if user and restaurant:
        items = [item for item in restaurant.menu if item.item_id in item_ids]
        if items:
            order = Order(order_id=len(orders) + 1, user=user, restaurant=restaurant, items=items)
            orders.append(order)
            print(f"Order placed successfully! Total price: ghc{order.total_price}")
        else:
            print("No valid items selected.")
    else:
        print("User or Restaurant not found.")

# Example Usage
if __name__ == "__main__":
    while True:
        print("1. List Restaurants")
        print("2. Show Menu")
        print("3. Place Order")
        print("4. Exit")
        choice = input("Enter choice: ")
        
        if choice == '1':
            list_restaurants()
        elif choice == '2':
            restaurant_id = int(input("Enter Restaurant ID: "))
            show_menu(restaurant_id)
        elif choice == '3':
            user_id = int(input("Enter User ID: "))
            restaurant_id = int(input("Enter Restaurant ID: "))
            item_ids = list(map(int, input("Enter Item IDs (comma separated): ").split(',')))
            place_order(user_id, restaurant_id, item_ids)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")
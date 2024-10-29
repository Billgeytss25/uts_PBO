class PremiumUser:
    def __init__(self, username, email, user_id):
        self.username = username
        self.email = email
        self.user_id = user_id

    def view_product(self):
        print(f"{self.username} is viewing a product.")

    def add_to_cart(self):
        print(f"{self.username} added a product to the cart.")

    def apply_voucher(self):
        print(f"{self.username} applied a voucher.")

    def request_priority_support(self):
        print(f"{self.username} has requested priority support.")


class Seller:
    def __init__(self, username, email, user_id):
        self.username = username
        self.email = email
        self.user_id = user_id

    def add_product(self):
        print(f"{self.username} has added a new product.")

    def process_order(self):
        print(f"{self.username} is processing an order.")


# Membuat objek PremiumUser
premium_user = PremiumUser(username="buddy-Anduk", email="buddy22@example.com", user_id=101)

# Memanggil metode untuk objek PremiumUser
premium_user.view_product()
premium_user.add_to_cart()
premium_user.apply_voucher()
premium_user.request_priority_support()

# Membuat objek Seller
seller = Seller(username="sellerPro", email="seller@example.com", user_id=202)

# Memanggil metode untuk objek Seller
seller.add_product()
seller.process_order()

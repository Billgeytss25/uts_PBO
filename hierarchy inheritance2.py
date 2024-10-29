# Kelas parent / Super class
class User:
    def __init__(self, username, email, userId):
        self.username = username
        self.email = email
        self.userId = userId

    def login(self):
        print(f"{self.username} ({self.email}) berhasil login")

    def logout(self):
        print(f"{self.username} berhasil logout")


# Hierarchy inheritance
class Seller(User):
    def __init__(self, username, email, userId, store_name):
        super().__init__(username, email, userId)
        self.store_name = store_name
        self.products = []

    def add_product(self, product_name, price):
        self.products.append({'name': product_name, 'price': price})
        print(f"Produk '{product_name}' berhasil ditambahkan ke toko '{self.store_name}'.")

    def view_products(self):
        print(f"Daftar produk di toko '{self.store_name}':")
        for product in self.products:
            print(f"- {product['name']} : Rp{product['price']}")

class Admin(User):
    def __init__(self, username, email, userId):
        super().__init__(username, email, userId)

    def remove_user(self, user):
        print(f"Admin '{self.username}' telah menghapus pengguna '{user.username}'.")

    def view_all_users(self, users_list):
        print("Daftar seluruh pengguna:")
        for user in users_list:
            print(f"- {user.username} ({user.email})")

# Membuat objek seller dan admin
seller = Seller("joko_seller", "joko@seller.com", 1, "Toko Joko")
admin = Admin("admin_andi", "andi@admin.com", 99)

# Seller menambah produk
seller.add_product("Baju Batik", 150000)
seller.add_product("Kopi Luwak", 250000)

# Seller menampilkan produk
seller.view_products()

# Admin menghapus user
admin.remove_user(seller)

# Menampilkan seluruh pengguna (misalnya ada beberapa pengguna dalam sistem)
user_list = [seller, admin]
admin.view_all_users(user_list)

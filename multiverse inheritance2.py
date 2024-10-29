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

# Multilevel inheritance
class BasicUser(User):
    def __init__(self, username, email, userId, posts=0):
        super().__init__(username, email, userId)
        self.posts = posts  # Menyimpan jumlah postingan pengguna BasicUser

    def create_post(self):
        self.posts += 1
        print(f"{self.username} telah membuat postingan baru. Total postingan: {self.posts}")

    def view_posts(self):
        print(f"{self.username} memiliki {self.posts} postingan")

class PremiumUser(BasicUser):
    def __init__(self, username, email, userId, posts=0, premium_features=None):
        super().__init__(username, email, userId, posts)
        self.premium_features = premium_features if premium_features else []

    def add_premium_feature(self, feature):
        self.premium_features.append(feature)
        print(f"{feature} telah ditambahkan ke fitur premium untuk {self.username}")

    def view_premium_features(self):
        if self.premium_features:
            features = ", ".join(self.premium_features)
            print(f"Fitur premium untuk {self.username}: {features}")
        else:
            print(f"{self.username} belum memiliki fitur premium.")

# Contoh Penggunaan
user1 = BasicUser("johndoe", "johndoe@example.com", 101)
user1.login()
user1.create_post()
user1.view_posts()
user1.logout()

print("\n")

user2 = PremiumUser("janedoe", "janedoe@example.com", 102)
user2.login()
user2.create_post()
user2.add_premium_feature("Video Calls")
user2.add_premium_feature("Ad-free Experience")
user2.view_premium_features()
user2.view_posts()
user2.logout()

class User:
    def __init__(self, login, password):
        self.Login = login
        self.Password = password

    def __str__(self):
        return f"Login: {self.Login}, Password: {self.Password}"


users = [
    User("admin", "QWEasd123"),
    User("alice", "password111"),
    User("bob", "ale123"),
    User("john", "olegsib"),
    User("emma", "cherchil")
]

target_login = "emma"
target_password = "cherchil"

found_user = None
for user in users:
    if user.Login == target_login and user.Password == target_password:
        found_user = user
        break

if found_user:
    print("Найден пользователь:")
    print(found_user)
else:
    print(f"Пользователь с логином '{target_login}' и паролем '{target_password}' не найден.")

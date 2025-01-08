class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = hash(password)

    def set_password(self, old_password, new_password):
        if self.check_password(old_password):
            self.__password = hash(new_password)

    def check_password(self, password):
        return self.__password == hash(password)

account = UserAccount(username="DefaultUser", email="example@mail.ru", password="1234")
account.set_password(old_password="1234", new_password="ABCDE!@")
print(account.check_password("1234"))

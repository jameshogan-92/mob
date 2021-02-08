from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager

from database import Database
db = Database("test.db")

Builder.load_file("design.kv")

class LoginScreen(Screen):
    def login(self, username="", password=""):
        print(username)
        if db.checkCreds(username,password) == "correct":
            self.manager.transition.direction = "right"
            self.manager.current = "login_screen_success"
        else :
            print("Invalid credentials")

    def sign_up(self):
        self.manager.transition.direction = "right"
        self.manager.current = 'signup_screen'

class LoginScreenSuccess(Screen):

    def log_out(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"
    pass

class SignupScreen(Screen):
    def add_user(self, username,password):
        print("{} : {}".format(username,password))
        if db.createUser(username,password) != "Fail":
            self.manager.transition.direction = "right"
            self.manager.current = "signup_screen_success"

class SignupScreenSuccess(Screen):
    def go_to_login(self):
        self.manager.current = "login_screen_success"

class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    MainApp().run()

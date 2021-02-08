from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
import random

from database import Database
db = Database("test.db")

Builder.load_file("design.kv")

class LoginScreen(Screen):
    """Allow users to log in with username and password"""
    def login(self, username="", password=""):
        print(username)
        if db.checkCreds(username.strip(),password.strip()) == "correct":
            self.manager.transition.direction = "right"
            self.manager.current = "login_screen_success"
        else :
            self.ids.msgBar.text = "Invalid credentials entered"

            print("Invalid credentials")

    def sign_up(self):
        self.manager.transition.direction = "right"
        self.manager.current = 'signup_screen'

class LoginScreenSuccess(Screen):
    """After successful log in"""
    def getRandom(self,file):
        with open("quotes/{}.txt".format(file), encoding="utf8") as quotesFile:
            quotes = quotesFile.read().split("\n")
            # for quote in quotes:
            #     print(quote)
            result = quotes[random.randint(0,len(quotes)-1)]
            print(result)
            self.ids.result_bar.text = result
            

    def get_quote(self, ans):
        print(ans)
        self.getRandom(ans)

    def log_out(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"


class SignupScreen(Screen):
    """Allow users to register with username and password"""
    def add_user(self, username,password):
        print("{} : {}".format(username,password))
        if db.createUser(username,password) != "Fail":
            self.manager.transition.direction = "right"
            self.manager.current = "signup_screen_success"


class SignupScreenSuccess(Screen):
    """For when users have successfully registered"""
    def go_to_login(self):
        self.manager.current = "login_screen_success"



class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    MainApp().run()
